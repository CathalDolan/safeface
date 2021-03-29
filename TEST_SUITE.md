# 5 Testing

## 5.1 Devices
Emulator used
- PC 
- IPad (768 x 1024px)
- Surface Du0 (540 x 720px)
- iPhone 6/7/8 Plus (414 x 736px)
- iPhone 5 (320 x 568px)

## 5.2 Known Bugs
1. Blah

## 5.3 Linting
Each piece of code was put through a "checker" to review the quality of the code.

### 5.3.1 HTML
- Website: https://validator.w3.org/nu/#textarea
- Result: All code passed, primarily with the exception of lines containing Jinja2 code. An repeated ID error was also ignored because the line of code is added dynamically and only one of the lines of code will be included.

### 5.3.2 CSS
- Website: https://jigsaw.w3.org/css-validator/validator
- Result: No errors or issues found

### 5.3.3 JavaScript
- Website: https://jslint.com/
- Result: Instances of "Double Quotes" ignored as a decision was made to use single quotes

### 5.3.4 Python
- Website: http://pep8online.com/
- Results: No errors or issues found


# 1 Header
- 1 - If a User is not logged in, is "Register/Login" link displayed?
- 1.1 - Does clicking the link open a drop down
- 1.2 - Does the dropdown contain
    - Register link
    - Login Link
- 1.3 - As a new User is "Cart Empty" displayed
- 1.4 - If there are items in the cart, is the total displayed
- 1.5 - If there are items in the cart, does clicking the total bring the user to the shopping cart 
- 1.6 - Does clicking the header logo bring the User to the home page
- 1.7 - On mobile devices with screens below 375, do My Account and Cart sit on opposite sides of the screen

# 2 Register
- 2.1 - Does clicking the Register link bring me to the "Sign Up" page
- 2.2 - Does clicking the "sign in" above the form link bring me to the "Sign In" page
- 2.3 - Can I add my data into each of the sign up fields
- 2.4 - Do I get an error if any of the fields are empty
- 2.5 - Clicking the Sign Up Button
    - 2.5.1 - Am I brought to a page "Verify Your Email Address"
    - 2.5.2 - Do I receive an email confirmation email
    - 2.5.3 - Does clicking the link bring me to a "Confirm E-Mail Address" page
    - 2.5.4 - Does clicking "Confirm" bring me to the sign in page
    - 2.5.5 - Is a new User added to the Admin section
- If I had products in my cart prior to signing up does the total still display in the header
- If I had products in my cart prior to signing up do I get a "Success" toast

# 3 Login
- 3.1 - Does clicking the Login link bring me to the "Sign In" page
- 3.2 - Does clicking the "sign up" above the form link bring me to the "Sign Up" page
- 3.3 - Can I add my data into each of the sign up fields
- 3.4 - Do I get an error if any of the fields are empty
- 3.5 - Does clicking the "Sign In " button sign me in and bring me to the home page
- 3.6 - Does completing the sign up process add me to the database
- 3.7 - If I had added products to a cart prior to signing in, does a toast display showing the products

# 4 Nav and Search Bar
- 4.1 - Does clicking each of the links bring me to the correct section
- 4.2 - Do the categories display as a hamburger dropdown on small devices
- 4.3 - Does putting a search term into the search field yeield a set of results
- 4.4 - If I leave the search input empty does a notification display
- 4.5 - If I leave the search input empty does the system return all products 
- 4.6 - If I search a term that is not in the database, does the search results yield "0" products in the count

# 5 Footer Newsletter
- 5.1 - Will the field accept email addresses only
- 5.2 - If I add a new address do I receive a notification
- 5.3 - If I add a new address is it added to the database
- 5.4 - If I add an existing email address do I receive a notification telling me such
- 5.5 - If I leave the input blank but submit, do I receive a notification?

# 6 "Back to Top" Button 
- 6.1 - Does the button display when I scroll down the page 
- 6.2 - Does clicking the button return the user to the top of the page 

# 7 Home Page
- 7.1 - Does the carousel produce a stream of images
- 7.2 - Does clicking the "More" button bring the user to that category of products
- 7.3 - Is the "More" button removed on small devices
- 7.4 - Does clicking on each of the categories in the "Mask Categories" section bring the user to the appropriate category page


# 8 Products / Search Results Page
- 8.1 - Does clicking the sort input display a dropdown
- 8.2 - Does sort by price work in both directions
- 8.3 - Does sort by name work in both directions
- 8.4 - Does clicking on a product image or name bring the user to that product's page
- 8.5 - Does clicking the "Quick Add" button display a toast confirming that the moq for that product has been added to the cart 
- 8.6 - Does the toast include: 
    - Product image
    - Name
    - Quantity added
    - Unit price
    - Total price
    - Cart button
    - Checkout button
    - An X button to close it
- 8.7 - Where there are multiple items in the cart, is each one listed on the toast
- 8.8 - Does clicking the "Cart" button bring the user to the Cart page 
- 8.9 - Does clicking the "Checkout" button bring the user to the Checkout page
- 8.10 - Where I land on the page from a "Search", is the term displayed at the top of the page 
- 8.11 - Where I land on the page having clicked a category, is the category name displayed at the top of the page 
- 8.12 - Is the count for the number of products displayed, shown 
- 8.13 - On PC are the products displayed 3 across
- 8.14 - On tablet are the products displayed 2 across 
- 8.15 - On mobile are the products displayed one beneath the other

# 9 Individual Product Page 
- 9.1 - Does clicking the image open an enlarged version in a new tab
- 9.2 - Does clicking on or hovering over a thumbnail image, enlarge it 
- 9.3 - Does clicking the "increment" button increase the quantity in multiples of the lowest price quantity (MOQ - Minimum order quantity)
- 9.4 - Does clicking the "decrement" button decrease the quantity in multiples of the moq 
- 9.5 - I cannot decrement below 0
- 9.6 - If I manually type a number that is not a multiple of the moq and I click the "Add" button, does a warning display
- 9.7 - If I leave the field empty and click "Add" do I get a warning 
- 9.8 - Does clicking the "Add" button when the quantity is legal, produce a toast
- 9.9 - Does the toast include: 
    - Product image
    - Name
    - Quantity added
    - Unit price
    - Total price
    - Cart button
    - Checkout button
    - An X button to close it
- 9.10 - Does clicking the "Back" button bring the user to the previous page they navigated from be that a category or search results 
- 9.11 - Does the page sections display one beneath the other on small screens

# 10 Shopping Cart 
- 10.1 - Does clicking the "increment" button increase the quantity in multiples of the lowest price quantity (MOQ - Minimum order quantity)
- 10.2 - Does clicking the "decrement" button decrease the quantity in multiples of the moq 
- 10.3 - I cannot decrement below 0
- 10.4 - If I manually type a number that is not a multiple of the moq and I click the "Add" button, does a warning display
- 10.5 - If I leave the field empty and click "Add" do I get a warning 
- 10.6 - Does the "Update" button display if I alter the quantity 
- 10.7 - Does clicking "Delete" remove a product from the shopping cart 
- 10.8 - Does the Pricing section remain fixed on medium larger screen devices and position at the bottom of the page on smaller screens 
- 10.9 - Does clicking "Checkout" bring the user to the Checkout page 
- 10.10 - Does clicking the "Keep" shopping button bring the user to a page with all products displayed
- 10.11 - If the products sub-total is below €100, does a "Free Delivery " notice display
- 10.12 - Does the notice say how much extra must be spent to achieve free delivery  

# 11 Checkout Page 
- 11.1 - Does the page contain a pricing section
    - Product image
    - Name
    - Quantity added
    - Product sub total 
    - Order sub total
    - Delivery cost
    - Net total 
    - VAT amount
    - Gross total 
- 11.2 - Is the sub-total equal to all of the product totals combined 
- 11.2 - If the sub-total is below €100, is the delivery charge €10.00
- 11.3 - If the sub-total is above €100, is the delivery charge €0.00
- 11.4 - Is the Net total the sum of sub-total and delivery 
- 11.5 - Is the VAT amount, 23% of the net total 
- 11.6 - Is the gross total, the sum of the net total and VAT 
- 11.7 - Can I add data to each of the fields?
- 11.8 - Can I only add numbers to the "Phone Number" field
- 11.9 - Can I only add email to the Email Address field 
- 11.10 - If I leave a compulsory field empty and click "Pay Now" does the offending field highlight 
- 11.11 - Does clicking the Country field produce a dropdown list of countries 
- 11.12 - Does clicking "Create an Account" bring the User to the create an account field 
- 11.13 - Does clicking login link bring the user to the login page
- 11.14 - Does the amount the user is due to be charged display beneath the credit card field 
- 11.15 - Does clicking "Back to Cart" button return me to the Shopping Cart page 
- 11.16 - Pay Now Button, does clicking it:
    - 11.16.1 - Produce a waiting spinner onscreen
    - 11.16.2 - Display a toast with the order number and email address 
    - 11.16.3 - Bring the user to a "Thank You" order confirmation page 
    - 11.16.4 - Send an email confirmation to the user 
        - Test for signed in user
        - Test for non-logged in user 
    - 11.16.5 - Add the order to the admin 
    - 11.16.6 - Process the payment so that it is visible in Stripe Payments 
    - 11.16.7 - Create the three payment webhooks in Stripe 
- 11.17 - If I have an address saved to my Profile already from a previous order, does that data auto-fill the Details and Delivery fields 

# 12 Order Confirmation Page 
- 12.1 - Does the page include:
    - Email order confirmation was sent to 
    - Order Number 
    - Order date and time
    - Product(s) name(s)
    - Quantity of each product ordered 
    - Products total 
    - Delivery cost 
    - Net amount 
    - VAT amount 
    - Gross total 
    - Full name 
    - Company name 
    - Department 
    - Address 1
    - Address 2
    - Town or City 
    - County or State
    - Postcode or Zip 
    - Country
    - Phone Number 
    - "Home" button (If non-logged in user)
    - "Profile" button (If logged in user)
- 12.2 - If Address 2 was left empty in the Checkout page, it doesn't display

# 13 Profile 
- 13.1 - If I completed a previous order and clicked the "Save details" checkbox on the Checkout page, are those details displayed under "My Details"
- 13.2 - If I change any data and click "Update Info", do those changes save onscreen
- 13.3 - If I change any data and click "Update Info", do those changes save in the database 
- 13.4 - Is my order history displayed 
- 13.5 - Is the order history displayed, newest at the top, oldest at the bottom 
- 13.6 - Does the order history include 
    - Order Number 
    - Date 
    - Items 
    - Order Total 
- 13.7 - Does clicking on the order number open the order 
- 13.8 - Does the order page match the Order Confirmation page 
- 13.9 - Does a toast display to confirm this is a past order 
- 13.10 - Does the toast include the order number 

# 14 Logout
- 14.1 - If I am logged in, when I click "My Account" do I get the "Logout" option 
- If I click Logout am I brought to a logout confirm page 
- If I confirm logout, am I logged out 
- If I had products in my cart prior to logging out, when I do, does the cart display Empty 