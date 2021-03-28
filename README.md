# Contents
[1 Introduction](#1-introduction)
[2 UI & Design](#2-ui-and-design)
[3 Site Content](#3-site-content)
[4 Technolgies & Third Party Plugins Employed](#4-technolgies-and-third-party-plugins-employed)
[5 Third Party Code Used](#5-third-party-code-used)


## External Readme files
Due to the volume of information required for certain Readme sections, they have been given a file of their own:
- Stripe Integration
- Deployment
- Test_Suite



# 1 Introduction
[Back to Contents](#contents)

Safe Face is my fourth milestone project for the Code Institute "Full Stack Software Development Diploma". It's
principal purpose is to demonstrate my abilities and knowledge of working with and combining HTML, CSS, Javascript 
and Python languages, while working with the Django framework, a database and Stripe payments integration. The basic
layout, functionality and structure is based on Code Institute's ["Ado Boutique"](https://github.com/ckz8780/boutique_ado_v1)
Full Stack Frameworks With Django project.

## 1.1 What is Safe Face
Safe Face is a b2b (Business to Business) website that allows businesses to purchase protective face masks in a
straight forward manner.

## 1.2 Why will Users use it?
The site is constructed in such a way that navigating it feels natural and intuitive to the user. The categories
are laid out clearly with multiple routes to see the products contained within them. The products themselves are 
presented so as to allow users to make an informed decision about whether to purchase. Once that decision has 
been made, it is a straight forward process to select a quantity and then checkout using Stripe payments.


# 2 UI and Design
[Back to Contents](#contents)

Owing to the nature of the products being sold on the site, the design needs to create an instant sense of
trust with the user. This is done via a combination of colours, typography, imagery and by providing lots of space
without compromising on providing essential product information. 

## 2.1 Colour Pallete
The main blue colour used is the Pantone Colour of the Year 2020; ["PANTONE 19-4052 Classic Blue"](https://www.pantone.com/eu/en/articles/color-of-the-year/color-of-the-year-2020).
As the website is medical based, a colour that creates the perception of cleanliness is essential.
Blue does exactly this, with the shade chosen also instilling calmness, confidence and a sense
of connection. The secondary colours associated with the blue, reinforce this perception, with the
green in particular complimenting the the sterility of the blue, while the other colours enhance
the sense of calmness.

## 2.2 Fonts
Two fonts were chosen for this project, both taken from Google Fonts, https://fonts.google.com/. 
- Open Sans was selected for content
- Oswald used for headings

Both were picked because of their regular use in medical websites. With 29% of all hospitals sites 
using Open Sans and 3% using Oswald, employing them here creates a sense of familiarity that builds 
trust with the user.
(https://www.ilovewp.com/resources/medical/wordpress-for-hospitals/most-used-google-fonts-on-hospital-websites/)

## 2.3 Imagery
So as to avoid clutter and thus maintain and sense of "cleanness", very limited imagery is
employed. This gives the site an opportunity to breath, so that the strong colours and fonts
come through. However, this means that where non-product imagery is used, it needs to very 
strongly reinforce the message of trust. For this reason, strong, trustworthy images of people
in masks are used. The images were sourced from:
- Images: https://www.pexels.com/
- Logo: https://www.freepik.com/premium-vector/face-mask-logo-template_11055254.htm 


# 3 Site Content
[Back to Contents](#contents)

## 3.1 Index/Home
Blah Blah
- Wireframes
    -- Desktop
    -- Tablet
    -- Mobile

## 3.2 Category Pages

## 3.3 Product Info Pages

## 3.4 Shopping Cart  

## 3.5 Checkout 

## 3.6 Payment Confirmation

## 3.7 Registration

## 3.8 Login

## 3.9 Profile

## 3.10 Log Out


# 4 Technolgies and Third Party Plugins Employed
[Back to Contents](#contents)

## 4.2 Django:
The Django framework forms the backbone of the functional code and is used in conjunction with Python

## 4.3 Python:
As much as possible, functionality was created using Python.

## 4.4 Javascript:
Where functions could not be created in Python, Javascript was used. On occasion this also called for the use of JQuery. The latter is accessed bia CDN.

## 4.5 CSS:
The majority of styling of the HTML code is done with CSS, though certain Flask and Materialize code has it's own inbuilt styling.

## 4.6 HTML:
Basic site layout and structure is achieved with HTML. However, in conjunction with Flask, Jinja2 was extensively used: https://jinja.palletsprojects.com/en/2.11.x/.

## 4.7 Fontawesome:
Icons used throughgout the site, particularly on buttons, were sourced from Font Awesome https://fontawesome.com/

## 4.8 JQuery:
JQuery is employed to 


# 5 Third Party Code Used
[Back to Contents](#contents)

Several pieces of external code were used on the project. In some cases, the code was used pretty much exactly
as given. In other cases, significant changes were required.

- **Website Base Structure & Functionality:** https://github.com/ckz8780/boutique_ado_v1)
- **Home Page Carousel - With Indicators:** https://getbootstrap.com/docs/4.0/components/carousel/
- **Back to Top Button:** https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
- **Remove Number Input Default Arrows:** https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp
- **Image Gallery on Product_Info:** https://gosnippets.com/snippets/bootstrap-4-ecommerce-preview-product-with-images
- **Marketing Banner Ticker Tape:** https://bbbootstrap.com/snippets/bootstrap-scrolling-breaking-news-ticker-53214404
- **Preventing Users Manually putting in non-multiple numbers:** http://jsfiddle.net/nottrobin/vN3xK/
- **Back Buttons:** https://www.w3schools.com/JSREF/met_his_back.asp
- **Favicon:** https://www.youtube.com/watch?v=kEf1xSwX5D8



After restart from Github
pip3 install -r requirements.txt
pip3 freeze --local > requirements.txt  - after installing a new pip3?

Rewatch Products Set-up, Products Admin, 2nd Video in tutorials


# Version Control

Gitpod is used as the IDE for writing code. From there it is pushed to a remote repository on Github.
It is a public repo available on [(https://github.com/CathalDolan/safeface)].

Development employs the use of two principal branches; "master" and "dev". Work is carried out on the
dev branch and once complete it is merged with the master branch. NO WORK SHOULD BE CARRIED OUT ON 
THE MASTER BRANCH. As and when required, additional temporary branches were created from the dev
branch.

## New Branch Creation

1. Creation of dev branch and direct navigation to it:
    git checkout -b dev


## Written to Repo Process

1. Confirm you are on the correct branch:
    git checkout dev
2. Save changes: Click file "Save All"
3. Add changes: git add .
4. Commit changes: git commit -m "Comment: reason for commit"
5. Push changes to the repository:
    git push origin master
6. Go to Github                                                        Images and more instructions

## Other useful Git commands used:
- "git checkout branch_name": Switch to a different branch
- "git branch -d branch_name: Delete a branch if no conflicts (-D in place of -d if there are conflicts)
- "git status": Check that staus of additions and commits
- "git log --online": 
- "git branch -a": Show all active branches


# Interesting Bugs

## Bootstrap 5 incompatibility
Needed to change to 4.6.0 because some of the XYZ wouldn't work with latest changes

## allauth base.html
Where base.html must be mannually added to the allauth folder, the code needs to be transferred from 
allauth/accounts/base.html. Additionmal code then must be added to the latter. See 2.4 above.





# Interesting Bugs
- Cart "Update" Wouldn't work due to specificity
-- var form=$(this).prev('.updated-form');  became    var form = $(this).siblings("form"); solved by tutor support.

QUantity_input_script needed am else atatement to inc and dec from cart and product info pages. Also had to use https://www.w3schools.com/tags/att_data-.asp and item.product.id 


Issue with the Qty inpout field in Cart, I can add non-multiples. Known bug


http://jigsaw.w3.org/css-validator/validator