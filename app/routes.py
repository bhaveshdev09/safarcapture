from flask import Blueprint, render_template, request

router = Blueprint("main", __name__)


@router.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        return "Form submitted "
    return render_template("index.html")


@router.route("/", methods=["POST"])
def footer_contact_form():
    if request.method == "POST":
        print(request.form)
        return "Thanks for contacting"


@router.route("/about")
def about():
    return render_template("about.html")


@router.route("/destination")
def destination():
    return render_template("destination.html")


@router.route("/faq")
def frequently_asked_question():
    return render_template("faq.html")


@router.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
        return "Contact Form submitted "
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


@router.route("/base")
def base_render():
    return render_template("base.html")
