# Integrating Stripe

Core logic/payment flow for this comes from here:
    - https://stripe.com/docs/payments/accept-a-payment
CSS from here: 
    - https://stripe.com/docs/stripe-js
    

1. - Stripe.com
    - Create an account
2. - https://stripe.com/docs/payments/accept-a-payment
    - Custom Payment Flow
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_2.JPG)
    - Number 3: Collect Card Details - Set up Stripe elements
    - Copy the script and paste into {% block corejs %} in base.html
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_3.JPG)
3. Go to Checkout.html
    - Add postload js block and include block.super
        {% block postloadjs %}
            {{ block.super }}
        {% endblock %}
    - Add client secret and public key Json scripts
        {{ stripe_public_key|json_script:"id_stripe_public_key" }}
        {{ client_secret|json_script:"id_client_secret" }}
        <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>
    - Add the public key
        - Copy the publishable key from the dashboard
        - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_4.JPG)
        - Add it to Checkout Views Context
        - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_5.JPG)
    - Create new folder, js, in static on same level as css folder
        - Create file, stripe_elements.js
4. Add vars to stripe_elements.js (slice the ends to remove quotation marks)
    - var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    - var clientSecret = $('#id_client_secret').text().slice(1, -1);
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_6.JPG)
5. Add additional vars to stripe_elements.js
    - Public key var
        var stripe = Stripe(stripePublicKey);
    - Use it to create an instance of Stripe elements
        var elements = stripe.elements();
    - Use that to create a card element
        var card = elements.create('card', {style: style});
    - Mount the card to the card-element id
        card.mount('#card-element');
    - Image
6. Add JS inline styling
    - Copy basic styles from Stripe: https://stripe.com/docs/payments/integration-builder
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_7.JPG)
    - Insert into stripe_element.js above card var and card.mount
        - Make changes as required
        - Add style to the card.var
        - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_8.JPG)
7. Add Stripe default CSS to Checkout.css
    ```
    /* Stripe Components */
    .StripeElement,
    .stripe-style-input {
    box-sizing: border-box;
    height: 40px;
    padding: 10px 12px;
    border: 1px solid transparent;
    border-radius: 0px;
    background-color: white;
    box-shadow: 0 1px 3px 0 #e6ebf1;
    -webkit-transition: box-shadow 150ms ease;
    transition: box-shadow 150ms ease;
    }

    .StripeElement--focus,
    .stripe-style-input:focus,
    .stripe-style-input:active {
    box-shadow: 0 1px 3px 0 #cfd7df;
    }

    .StripeElement--invalid {
        border-color: orange;
    }

    .StripeElement--webkit-autofill {
    background-color: #fefde5 !important;
    }

    .stripe-style-input::placeholder {
        color: #aab7c4;
    }
    ```
8. Take advantage of Stripe Style input class
    - Add stripe style input to all relevant fields in forms.py
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_9.JPG)
    - Add the class to the checkout css
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_10.JPG)
9. Add the JS to the checkout html within block postloadjs
    - <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>
10. Include the input in Checkout.html
    - <input type="hidden" value="{{ client_secret }}" name="client_secret">
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_11.JPG)
11. Add a listener for card errors in Stripe_elements.js
    -![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_13.JPG)
    ```
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });
    ```
12. Provide total cost and amount to be charged to Stripe via Checkout Views
    - Import cart_contents from the cart contexts 
        from cart.contexts import cart_contents
    - Inject the data into the checkout function and calculate gross_total
        current_cart = cart_contents(request)
        total = current_cart['gross_total']
        stripe_total = round(total * 100)
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_14.JPG)
13. Install Stripe
    - pip3 install stripe
    - Import into views beneath cart_contents
        import stripe
    - Also import settings just below messages
        from django.conf import settings
14. Add stripe reqs to settings.py inclu currency and key access
    - STRIPE_CURRENCY = 'eur'
    - STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    - STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
15. Export the keys using the cli
    - On Stripe dash copy the "publishable key"
    - In cli: export STRIPE_PUBLIC_KEY=copied code
    - On Stripe dash copy the "secret key"
    - In cli: export STRIPE_SECRET_KEY=copied code
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_15.JPG)
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_16.JPG)
    - Each time the workspace is restarted this must be repeated.
    - export STRIPE_WH_SECRET=copied code
16 . Create Payment Intent in Checkout Views
    - Add the keys at the top of teh function:
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
    - Set the secret key on stripe
        stripe.api_key = stripe_secret_key
    - Create the payment Intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_17.JPG)
17 . Update Context and add key warning
    - In Context:
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    - Warning to alert us if we forget to set public key
        if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
        template = 'checkout/checkout.html'
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_18.JPG)
18 . Add event listener to...
    - From https://stripe.com/docs/payments/accept-a-payment?ui=elements go to section 4 and copy the client.js
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_19.JPG)
    - Paste into stripe_elements.js
    - Prevent multiple submissions. Add code to the Stripe code:
        card.updated({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
    - Inject the error message into the card error div:
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
    - Insert form submission method:
        form.onsubmit();
    - Add error var:
        var errorDiv = document.getElementById('card-errors');
    - If there's an error Re-enable the card element and submit button:
        card.updated({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
    - If no error submit the form:
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    - ![CI logo]({{ MEDIA_URL }}stripe_md_images/stripe_20.JPG)