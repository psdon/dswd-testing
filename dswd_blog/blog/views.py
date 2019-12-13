from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import CreateBlog, EditBlog
from ..models import Blog
from ..extensions import db


bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/<int:page>")
@login_required
def home(page):
    blogs = Blog.query.order_by(Blog.id.desc()).paginate(per_page=5, page=page, error_out=True)
    # blogs = Blog.query.all()

    return render_template("blog/home/index.html", blogs=blogs)


@bp.route("/new/", methods=['GET', 'POST'])
@login_required
def create_blog():
    form = CreateBlog()

    if form.validate_on_submit():
        title = form.title.data
        content = form.title.data

        blog_obj = Blog(title=title, content=content, author=current_user)

        db.session.add(blog_obj)
        try:
            db.session.commit()
            return redirect(url_for('blog.home', page=1))
        except Exception as error:
            db.session.rollback()
            print(error)
            flash("Server error occured", "warning")

    return render_template("blog/create_blog/index.html", form=form)


@bp.route("/edit/<int:blog_id>", methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    blog_post = Blog.query.filter(Blog.author_id == current_user.id,
                                  Blog.id == blog_id).first_or_404()

    form = EditBlog()

    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.content = form.content.data

        try:
            db.session.commit()
            return redirect(url_for('blog.home', page=1))
        except Exception as error:
            db.session.rollback()
            print(error)
            flash("Server error occured", "warning")
    else:
        form.title.data = blog_post.title
        form.content.data = blog_post.content

    return render_template("blog/edit_blog/index.html", form=form)


@bp.route("/delete/<int:blog_id>", methods=['GET'])
@login_required
def delete_blog(blog_id):
    blog_post = Blog.query.filter_by(id=blog_id).first_or_404()

    db.session.delete(blog_post)
    try:
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        print(error)
        flash("Server error occured", "warning")

    return redirect(url_for('blog.home', page=1))