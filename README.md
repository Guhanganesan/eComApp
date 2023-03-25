# Django_E-Commerce_Web

# Installations

1. django-admin startproject E_Com_Web => create project
2. cd .\E_Com_Web\
3. python manage.py runserver
4. django-admin startapp myapp
5. hard refresh => ctrl+shift+all

# Models
1. python manage.py makemigrations
2. python manage.py migrate

# Create Super User

1.  Run => python manage.py createsuperuser         
2.  Username (leave blank to use 'admin'): guhan_test@gmail.com              
3.  Email address: guhan_test@gmail.com           
4.  Password: 1234      
5.  Password (again): 1234          
`This password is too short. It must contain at least 8 characters.         
This password is too common.    
This password is entirely numeric.      
Bypass password validation and create user anyway? [y/N]: y     
Superuser created successfully.`        

6. Run => python manage.py runserver        
7. check => http://127.0.0.1:8000/admin/        
8. add some products in admin sites and write views functions to display product details on products

# Bootstrap 4.2 

1. Navbar link: https://getbootstrap.com/docs/4.2/components/navbar/

# Reference

1. https://github.com/divanov11/ecom_steps/blob/master/prt6_stp4_main.css
2. Cart -1 : https://github.com/divanov11/ecom_steps/blob/master/prt8_stp3_cart.html
3. Checkout -1 : https://github.com/divanov11/ecom_steps/blob/master/prt9_stp4_checkout.html

# Icons

1. https://www.toptal.com/designers/htmlarrows/arrows/