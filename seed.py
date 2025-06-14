from app import create_app, db
from app.models import Product, GalleryImage

app = create_app()

with app.app_context():
    db.create_all()

    if Product.query.count() == 0:
        products = [
            Product(
                name="Lighter Vintage",
                description="Handcrafted retro styled lighter.",
                price=189.00,
                image_filename="lighter1.jpg",
            ),
            Product(
                name="Lighter Black Minimal",
                description="Handcrafted black styled lighter.",
                price=159.00,
                image_filename="lighter2.jpg",
            ),
            Product(
                name="Lighter Gold Lux",
                description="Handcrafted Prestige-Gold styled lighter.",
                price=249.00,
                image_filename="lighter3.jpg",
            ),
            Product(
                name="Lighter Silver Style",
                description="Handcrafted Silver, polished lighter.",
                price=179.00,
                image_filename="lighter4.jpg",
            ),
            Product(
                name="Lighter Black Matt",
                description="Handcrafted black, non-polished lighter.",
                price=139.00,
                image_filename="lighter5.jpg",
            ),
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()
        print("Products were added.")
    else:
        print("Products are already in db.")

    if GalleryImage.query.count() == 0:
        gallery_images = [
            GalleryImage(filename="g1.jpg", description="test gallery 1"),
            GalleryImage(filename="g2.jpg", description="test gallery 2"),
            GalleryImage(filename="g3.jpg", description="test gallery 3"),
            GalleryImage(filename="g4.jpg", description="test gallery 4"),
            GalleryImage(filename="g5.jpg", description="test gallery 5"),
        ]
        db.session.bulk_save_objects(gallery_images)
        db.session.commit()
        print("Gallery images were added.")
    else:
        print("Images are already in db.")
