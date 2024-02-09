from app.models import Destination, Package, State
from django.db.models import Count


def destination_list(request):
    destination_list_group_by_location = (
        Destination.objects.values("location")
        .annotate(Count("location"))
        .values_list("location", flat=True)
    )  # Queryset [Location i.e 'UK', 'MH']

    locations = list(map(lambda loc: State(loc), destination_list_group_by_location))

    destinations = (
        Destination.objects.only("id", "name", "location")
        .order_by("name")
        .values("id", "name", "location")
    )
    return {"destination_list": destinations, "locations": locations}


def package_list(request):
    package_lists = (
        Package.objects.only("id", "name", "days")
        .order_by("name")
        .values("id", "name", "days")
    )
    return {"package_list": package_lists}
