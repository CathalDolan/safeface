# Contents
- [1 Introduction](#1-introduction)
- [2 UI & Design](#2-ui-and-design)
- [3 Site Content](#3-site-content)
- [4 Technolgies & Third Party Plugins Employed](#4-technolgies-and-third-party-plugins-employed)
- [5 Third Party Code Used](#5-third-party-code-used)
- [6 Version Control](#6-version-control)
- [7 Bugs and Hacks](#7-bugs-and-hacks)
- [8 Future Functionality](#8-future-functionality)


## External Readme files
Due to the volume of information required for certain Readme sections, they have been given a file of their own:
- [Project Setup](https://github.com/CathalDolan/safeface/blob/master/PROJECT_SETUP.md)
- [Stripe Integration](https://github.com/CathalDolan/safeface/blob/master/STRIPE_INTEGRATION.md)
- [Deployment](https://github.com/CathalDolan/safeface/blob/master/DEPLOYMENT.md)
- [Test_Suite](https://github.com/CathalDolan/safeface/blob/master/TEST_SUITE.md)



# 1 Introduction
[Back to Contents](#contents)

Safe Face is my fourth milestone project for the Code Institute "Full Stack Software Development Diploma". It's
principal purpose is to demonstrate my abilities and knowledge of working with and combining HTML, CSS, Javascript 
and Python languages, while working with the Django framework, a database and Stripe payments integration. The basic
layout, functionality and structure is based on Code Institute's ["Ado Boutique"](https://github.com/ckz8780/boutique_ado_v1)
Full Stack Frameworks With Django project.

The site was constructed over a period of 5 weeks between February and March 2021.

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

## 2.4 Page Layout
Every page retains a consistency in layout and design so as to increase familiarity with the site as the user
progresses through it. This includes:
- **Title:** Each page has a large H1 header, underscored by a contrasting rule
- **HR's:** Rules are used throughout to separate the page sections and thus make it easier for users to 
clearly see the information displayed.
- **Section Headings:** All section headers use the same size heading, as do any sub-sections or sections of
not.
- **Images:** All images are created to the same size, dimensions and resolution, each set on a clean white
background.


## 2.5 User Stories
A series of User Stories were create to guide Development
![USer Stories 1](https://i.imgur.com/61rlkXq.jpg)
![USer Stories 2](https://i.imgur.com/cxmFCYQ.jpg)
![USer Stories 1](https://i.imgur.com/xiFkgTm.jpg)


# 3 Site Content
[Back to Contents](#contents)

## 3.1 Index/Home
As the first page users reach, it is important that the home page is attractive and catches the
user's attention. This is done in two ways, a moving carousel with hero images, and a "ticker
tape" style banner. So as to make navigation as easy as possible, users have four means by which
to get to the masks they want:
- 1. Navbar
- 2. Search
- 3. Hero Image
- 4. Mask Categories in the page content
- **Wireframes**
-- [Desktop](https://i.imgur.com/yxyvMby.jpg)
-- [Tablet](https://i.imgur.com/YLJtql2.jpg)
-- [Mobile](https://i.imgur.com/pszjOcD.jpg)

## 3.2 Login
The login page is imported from Django. The only change is some basic styling.
- **Wireframes**
-- [Desktop](https://i.imgur.com/sXAU57v.jpg)
-- [Tablet](https://i.imgur.com/KFDHCGS.jpg)
-- [Mobile](https://i.imgur.com/X4RQeO7.jpg)

## 3.3 Registration
The registration page is imported from Django. The only change is some basic styling.
- **Wireframes**
-- [Desktop](https://i.imgur.com/BvLbF89.jpg)
-- [Tablet](https://i.imgur.com/b5Ywt23.jpg)
-- [Mobile](https://i.imgur.com/QjCAEjK.jpg)

## 3.4 Product Group / Search Results
Users land on a product group page when they select a mask category or compleyte a search.
- **Sections & Components:**
    - H1
    - # of product displayed
    - Sort widget
        - Price 0-9 / 9-0
        - Name a-z / z-a 
    - HR
    - Text
    - Product Cards
        - Product Image
        - Product Name (links to that product page)
        - Code
        - Category 
        - Unit Price Range, lowest to highest
        - Quick Add Button: Adds the minimum order quantity to the cart
        - HR
    - VAT notification
- **Wireframes**
-- [Desktop](https://i.imgur.com/ZPSnviV.jpg)
-- [Tablet](https://i.imgur.com/N8n9krS.jpg)
-- [Mobile](https://i.imgur.com/W2jc93F.jpg)

## 3.5 Product
The product page allows users to view all available information about the product.
- **Sections & Components:**
    - H1
    - HR
    - Product Image
        - 1 main image
        - 3 thumbnails. Clicking a thumbnail displays a large version
    - Details
        - Description
        - Code 
        - Category 
    - HR
    - Spec Essentials
        - Certification
        - Standard
        - dimensions
        - Material
    - Pricing
        - 5 Price breaks
    - Ordering
        - Quantity input with increment and decrement buttons
            - Products on decrement according to the product minimum order quantity
        - Add Button
        - Back Button
- **Wireframes**
    -- [Desktop](https://i.imgur.com/Ltt3Xfh.jpg)
    -- [Tablet](https://i.imgur.com/Fu81rba.jpg)
    -- [Mobile](https://i.imgur.com/YfWaIE8.jpg)

## 3.6 Shopping Cart
The shopping cart allows the user to view all of the products theyhave selected, and the essential purchase
information for each.
- **Sections & Components:**
    - H1
    - HR
    - Product Section 
        - Product Image
        - Product Name
        - Code
        - Quantity input with increment and decrement buttons
            - Products on decrement according to the product minimum order quantity
        - Unit Price
        - Total 
    - HR
    - Pricing Section
        - Sub-Total
        - Delivery 
        - Net 
        - VAT 
        - HR
        - Gross
        - Checkout Button
        - Keep Shopping Button 
    - VAT Notification
- **Wireframes**
    -- [Desktop](https://i.imgur.com/fKdrjEr.jpg)
    -- [Tablet](https://i.imgur.com/X9NYt5z.jpg)
    -- [Mobile](https://i.imgur.com/N942oV1.jpg)

## 3.7 Checkout
- **Sections & Components:**
    - H1
    - HR
    - Text 
    - Details
        - Full Name 
        - Phone 
        - Department
    - Delivery 
        - Company Name 
        - Email 
        - Address 1
        - Address 2
        - Town or City 
        - County or State 
        - Postcode
        - Country
            - Populated via Django import so as to match Stripes 2 character country codes in the backend
        - Option to save data to Profile
        - Payment 
            - Credit Card Input 
            - Total to be debited 
        - Pay Now Button 
        - Back to Cart Button 
    - Order Summary
        - Product thumbnail
        - Product Name 
        - Subtotal 
        - Quantity Ordered 
        - HR
        - Sub-total 
        - Delivery 
        - Net Total 
        - VAT 
        - Gross Total: 
- **Wireframes**
    -- [Desktop](https://i.imgur.com/e0481ub.jpg)
    -- [Tablet](https://i.imgur.com/tOjrvQT.jpg)
    -- [Mobile](https://i.imgur.com/ILA6EH8.jpg)

## 3.8 Order Confirmation
Once a user completes a purchase they are brought to the order confirmatiomn page. It 
contains all data relating to the order. It also acts as the order history page when a
user accesses an historical order from their Profile.
- **Sections & Components:**
    - H1
    - HR
    - Text 
    - Order Info 
        - Order Number 
        - Order Date 
    - Order Details 
        - Product Name 
        - Quantity of each product 
    - Billing Info 
        - Products Total 
        - Delivery 
        - Net 
        - VAT 
        - Gross Total 
    - Delivering to:
        - Full Name 
        - Company 
        - Department 
        - Address 1
        - Address 2
        - Town or City 
        - County or State 
        - Postcode
        - Country
        - Phone Number
    - Home Button / Profile Button 
- **Wireframes**
    -- [Desktop](https://i.imgur.com/oLkRw5c.jpg)
    -- [Tablet](https://i.imgur.com/zzPIYVa.jpg)
    -- [Mobile](https://i.imgur.com/d40Rn5q.jpg)

## 3.9 Profile
- **Sections & Components:**
    - H1
    - HR
    - My Details 
        - Name 
        - Email 
        - Phone Number 
        - Company Name 
        - Department 
        - Address 1 
        - Address 2
        - Town or City 
        - County or State 
        - Postcode
        - Country
    - Update Info
    - Order History 
        - Order Number 
        - Date 
        - Items 
        - Order Total 
- **Wireframes**
    -- [Desktop](https://i.imgur.com/09XqNoJ.jpg)
    -- [Tablet](https://i.imgur.com/cg2LxWn.jpg)
    -- [Mobile](https://i.imgur.com/oYiMUUJ.jpg)


# 4 Technolgies and Third Party Plugins Employed
[Back to Contents](#contents)

## 4.2 [Django](https://www.djangoproject.com/):
The Django framework forms the backbone of the functional code and is used in conjunction with Python

## 4.3 [Python](https://www.python.org/):
As much as possible, functionality was created using Python.

## 4.4 [Javascript](https://www.javascript.com/):
Where functions could not be created in Python, Javascript was used. On occasion this also called for the use of JQuery. The latter is accessed bia CDN.

## 4.5 [CSS](https://www.w3schools.com/css/):
The majority of styling of the HTML code is done with CSS, though certain Flask and Materialize code has it's own inbuilt styling.

## 4.6 [HTML](https://www.w3schools.com/html/):
Basic site layout and structure is achieved with HTML. However, in conjunction with Flask, Jinja2 was extensively used: https://jinja.palletsprojects.com/en/2.11.x/.

## 4.7 [Fontawesome](https://fontawesome.com/):
Icons used throughgout the site, particularly on buttons, were sourced from Font Awesome 

## 4.8 [JQuery](https://jquery.com/):
JQuery library employed to make coding Javascript fast and easier


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


# 6 Version Control
[Back to Contents](#contents)

Gitpod is used as the IDE for writing code. From there it is pushed to a remote repository on Github.
It is a public repo available on [(https://github.com/CathalDolan/safeface)].

Development employs the use of two principal branches; "master" and "dev". Work should be carried out on the
dev branch and once complete it is merged with the master branch. As and when required, additional 
temporary branches are created from the dev branch.

- 6.1 - New Branch Creation
    - 6.1.1 - Creation of dev branch and direct navigation to it:
        git checkout -b dev

- 6.2 - Written to Repo Process
    - 6.2.1 - Confirm you are on the correct branch:
            git checkout dev
    - 6.2.2 - Save changes: Click file "Save All"
    - 6.2.3 - Add changes: git add .
    - 6.2.4 - Commit changes: git commit -m "Comment: reason for commit"
    - 6.2.5 - Push changes to the repository:
            git push origin master
    - 6.2.6 - Merge the branches in Github

- 6.3 - Other useful Git commands used:
    - 6.3.1 - "git checkout branch_name": Switch to a different branch
    - 6.3.2 - "git branch -d branch_name: Delete a branch if no conflicts (-D in place of -d if there are conflicts)
    - 6.3.3 - "git status": Check that staus of additions and commits
    - 6.3.4 - "git log --online": 
    - 6.3.5 - "git branch -a": Show all active branches


# 7 Bugs and Hacks
[Back to Contents](#contents)

-**7.1 - Interesting Bugs**
    - 7.1.1 - Bootstrap 5 incompatibility
        Several pieces of functionality required Bootstrap 4 as opposed to 5.
    - 7.1.2 - allauth base.html
        Where base.html must be mannually added to the allauth folder, the code needs to be transferred from 
        allauth/accounts/base.html. Additionmal code then must be added to the latter. See 2.4 above.
    - 7.1.3 - Cart "Update" wouldn't work due to specificity
        var form=$(this).prev('.updated-form');  became    var form = $(this).siblings("form"); solved by tutor support.
    - 7.1.4 - Quantity_input_script 
        Quantity_input_script needed am else atatement to inc and dec from cart and product info pages. Also had to use
        https://www.w3schools.com/tags/att_data-.asp and item.product.id 

- **7.2 - Known Bugs**
Due to the time restraints on creating and submitting the project, there are several known bugs that were left
unfixed. While the severity of the bugs ranges from minor to having a reasonable impact on User Experience,
none prevent the user from using the site, and non impact on the user's experience so much that they wouldn
opt not to use the site.
    - 7.2.1 - Cart: Input Quantity
        Users can manually input any quantity rather than being restricted to the quantity breaks stipulated.
        Implemented on teh Product Info page, but unable to replicate in the Cart
    - 7.2.2 - Cart: Full Name
        The user's full name is not displaying in the cart when the User is logged in.
    - 7.2.3 - Checkout Emails
        The order confirmation email is only being sent to non-logged in users. Logged in users do not receive it.
    - 7.2.4 - User Profile
        The user's full name and email address are not displaying in the Profile 
    - 7.2.5 - Individual Product Page 
        If user manually clears the quantity input and tries to add to the order, an error page displays
    - 7.2.6 - User Registration 
        Where a User inputs a password in the incorrect format, they are not given an indication as to what is wrong. 
        Instead the notice states that the existing passwords match, which is not the case.
    - 7.2.7 - Email Sending Speed
        Emails take up to 5 minutes to reach the recipient's inbox. While this is an external issues, investigation
        is required to correct the problem
    - 7.2.8 - Product Info Page Thumbnail ID'section
        The same ID's are repeated on both sets of thumbnails. While this causes a linting error, neither 
    - 7.2.9 - Shopping Cart 
        User can only update the top quantity. This is due to the targetting of the ID in the code. Needs to be
        updated to target an alternative tag.

- **7.3 - Hacks**
    - 7.3.1 - My Account & Cart in Header on Mobile
        For aesthetic purposes, on mobile view the My Account and Cart links were not included in the hamburger menu.
        This caused issue because there is not space on the right side of the logo for both links, so they needed to 
        be positioned either side of it. However, because they two links are part of teh same list, doing so was 
        problematic. The hack to solve the issue, was to give My Account a margin-right, the sixe of which was 
        dictated by the screen size.
    - 7.3.2 - Home Page Hero Images Text
        Owing to the nature of the images selected, a dark text didn't work on some of them. However, a lighter text
        wouldn't have worked on many, and a light text wouldn't work on any. To counteract this, a semi-transparent
        layer was added behind the text to make the text and button stand out on all images.


# 8 Future Functionality
[Back to Contents](#contents)
- 8.1 - **Google Maps API**: Integrate Google Maps API so that users need only enter the business name or postcode and then
select from options presented
- 8.2 - **Social Media Sign In**: Allow users to sign up and sign in via their social media account
- 8.3 - **Static Pages**: A variety of static pages are required, each accessed from the footer:
    - About Use
    - Contact Us
    - Returns
    - GDPR Compliance and Privacy Policy
    - Copyright Compliance
    - Terms & Conditions
- 8.4 - **Additional Payment Options**:
    - Apple Pay
    - Paypal