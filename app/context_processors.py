from app.models import Destination, Package


def destination_list(request):
    destinations = (
        Destination.objects.only("id", "name").order_by("name").values("id", "name")
    )
    return {"destination_list": destinations}


def package_list(request):
    package_lists = (
        Package.objects.only("id", "name", "days")
        .order_by("name")
        .values("id", "name", "days")
    )
    return {"package_list": package_lists}
