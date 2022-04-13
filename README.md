
Amazon Price Web Scrap
=============
Collect Historical Price Data From Amazon

Table of Contents
-----------------

-   [Project Background](#project-background)
-   [Install & Setup](#install-&-setup)
-   [Usage](#usage)
-   [Authors](#authors)
-   [License](#license)

Project Background
----------

Collect historical price data for selected products in order to use it for analytical purposes.

Objective: show to a client the variation of price about one or more product.


Install & Setup
---------------
```html 
git clone https://github.com/ccallazans/price-web-scraping.git
cd price-web-scraping
```
Install required packages
```
pip install -r requirements.txt
```


Usage
-----

```
python src/app.py amazon_product_link
```
ex:
```
python src/app.py https://www.amazon.com.br/gp/product/B07FQK1TS9
```



Authors
-------

* Ciro Callazans | [@ccallazans](https://github.com/ccallazans)
* Leonardo José C. Pedreira Gama | [@Leonardopedreira](https://github.com/Leonardopedreira)


License
-------

[MIT License](LICENSE)