import os
import django
import sys

# Set up django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grielisha.settings')
django.setup()

from products.models import Product, Category
from services.models import Service

def seed_data():
    print("Clearing old data...")
    Category.objects.all().delete()
    Product.objects.all().delete()
    Service.objects.all().delete()

    # --- Categories ---
    cat_cleaning = Category.objects.create(name="Cleaning Supplies", description="Professional grade cleaning solutions")
    cat_detailing = Category.objects.create(name="Car Detailing", description="Premium car care products")
    cat_digital = Category.objects.create(name="Digital Services", description="Cutting-edge software and design")

    # --- Products ---
    print("Seeding Products...")
    Product.objects.create(
        name="Grielisha Nano-Coating Pro",
        description="High-performance ceramic coating for automotive surfaces. Provides 12 months of hydrophobic protection.",
        price=7500.00,
        category=cat_detailing,
        category_type='product',
        stock_quantity=25,
        is_featured=True,
        tags="Trending,Premium,Detailing",
        features=["9H Hardness", "Heat Resistance", "UV Protection", "High Gloss Finish"],
        specifications={"volume": "50ml", "application": "Sponge/Cloth", "cure_time": "24 hours"},
        rating=4.9,
        reviews_count=128
    )

    Product.objects.create(
        name="Industrial Multi-Surface Cleaner",
        description="Professional grade cleaner for offices and large commercial spaces.",
        price=3200.00,
        category=cat_cleaning,
        category_type='product',
        stock_quantity=50,
        tags="Best Seller",
        features=["Concentrated Formula", "Eco-Friendly", "Safe on Chrome", "Zero Residue"],
        specifications={"volume": "5L", "ph_level": "7.5 (Neutral)", "scent": "Lemon Fresh"},
        rating=4.7,
        reviews_count=45
    )

    # --- Services ---
    print("Seeding Services...")
    Service.objects.create(
        name="Executive Office Deep Cleaning",
        description="A comprehensive deep cleaning service for modern corporate environments.",
        service_type="office_cleaning",
        base_price=15000.00,
        duration_hours=6,
        is_featured=True,
        tags="Professional,Office",
        features=["Surface Disinfection", "Window Cleaning", "Carpet Shampooing", "Air Purification"],
        specifications={"team_size": "3 people", "equipment": "Industrial Vacuums", "chemicals": "Anti-Viral Grade"},
        rating=4.8,
        reviews_count=89
    )

    Service.objects.create(
        name="Dynamic Website Development",
        description="Build a high-performance, responsive website using modern technology stacks.",
        service_type="website_development",
        base_price=45000.00,
        duration_hours=40,
        is_featured=True,
        tags="Digital,Tech,SEO",
        features=["Responsive Design", "SEO Optimized", "Speed Focused", "CMS Integration"],
        specifications={"tech_stack": "React / Django", "delivery_time": "14 days", "revisions": "Unlimited"},
        rating=5.0,
        reviews_count=24
    )

    print("Successfully seeded the GRIELISHA ecosystem with REAL DATA.")

if __name__ == "__main__":
    seed_data()
