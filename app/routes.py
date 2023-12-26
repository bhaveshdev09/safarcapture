from flask import Blueprint, render_template

router = Blueprint("main", __name__)


@router.route("/")
def index():
    return render_template("index.html")


@router.route("/about")
def about():
    return render_template("about.html")


@router.route("/destination")
def destination():
    return render_template("destination.html")


@router.route("/faq")
def frequently_asked_question():
    return render_template("faq.html")


@router.route("/contact")
def contact():
    return render_template("contact.html")


@router.route("/blogs")
def blogs():
    return render_template("blogs.html")


@router.route("/blogs/detail/")
def blog_details():
    return render_template("blog_detail.html")


@router.route("/package")
def package():
    return render_template("package.html")
