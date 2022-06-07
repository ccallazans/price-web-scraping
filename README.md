
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
![Pipeline](/assets/pipeline.png "Pipeline")

Collect historical price data for selected products in order to use it for analytical purposes.
Save price data on S3 and local file system.

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
Install AWS Cli and configure access to s3
```
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```
Look the name gave by you in Amazon S3 Bucket and edit the variable "BUCKET_NAME" on connection.py.


Usage
-----

It can be used to collect the data from a group of links. Use the "src/products.json" file to edit these links
```
python src/app.py
```
It can be used to collect the data from an specific item.
```
python src/app.py amazon_product_link
ex:
python src/app.py https://www.amazon.com.br/gp/product/B07FQK1TS9
```



Authors
-------

* Ciro Callazans | [@ccallazans](https://github.com/ccallazans)
* Leonardo José C. Pedreira Gama | [@Leonardopedreira](https://github.com/Leonardopedreira)


License
-------

[MIT License](LICENSE)
