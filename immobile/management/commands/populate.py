import random
import string
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from immobile.models import Immobile, Reservation, Advertisement

def random_code(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        immobiles_code = ["CAS", "APA", "FLA", "SOB", "KIT", "LOf"]
        
        for im in range(0,5):

            random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

            Immobile.objects.create(
                code = f"{random.choice(immobiles_code)}{im}",
                guest_limit = random.randint(1,10),
                bathroom_count = random.randint(1,4),
                is_pet = bool(random.getrandbits(1)),
                cleaning_fee = random.uniform(100, 250),
                activation_date = random_date,
            )
        self.stdout.write(self.style.SUCCESS("Imoveis criados"))

        immobiles_list_ids = Immobile.objects.values_list('id', flat=True)
        platform_names = ["Airbnb", "TripAdvisor", "Homestay"]

        for ad in range(0,6):
            Advertisement.objects.create(
                immobile_id=random.choice(immobiles_list_ids),
                platform_name=random.choice(platform_names),
                platform_fee = random.uniform(10, 40),
            )
        self.stdout.write(self.style.SUCCESS("Anuncios criados"))

        advertisement_list_ids = Advertisement.objects.values_list('id', flat=True)
        date_start = datetime.now()
        
        for re in range(0,8):
            date_end = date_start + timedelta(days=re+10)
            Reservation.objects.create(
                code = random_code(),
                advertisement_id = random.choice(advertisement_list_ids),
                check_in = date_start,
                check_out = date_end,
                total_price = random.uniform(400, 1000),
                num_guests = random.randint(1,10)
            )
        self.stdout.write(self.style.SUCCESS("Anuncios criados"))