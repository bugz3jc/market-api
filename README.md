# market-api
This is a custom API used by The Market project. It is made with Python Flask and deployed on Google Compute Engine.

## End Points
### Products
  1. `GET - http://api.johncristayco.me/product/list` - Fetches all products
  2. `GET - http://api.johncristayco.me/product/sku/<product_sku>` - fetches a single product by SKU
  3. `GET - http://api.johncristayco.me/product/category/<category_id>` -fetches all products by category
  4. `GET - http://api.johncristayco.me/product/search/<keyword>` - searches for products by keyword

### Categories
  1. `GET - http://api.johncristayco.me/category/list` - Fetches all categories
  2. `GET - http://api.johncristayco.me/category/<product_id>` - Fetches all categories where a particular product belongs
