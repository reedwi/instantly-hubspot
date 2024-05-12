# Instantly HubSpot Integration
Project to allow for HubSpot and Instantly to work together. Add HubSpot contacts into Instantly campaigns and get details back in HubSpot.

[Data Model](https://app.eraser.io/workspace/UCgKtjzAOXFl24u4tXgW?origin=share)

## Install Flow
Where everything starts during the install flow
1. User goes to Stripe checkout page and completes flow
2. Stripe webhook sends to /payments and we create a payment record
3. Stripe redirects to the HubSpot app install with a state param of the stripe checkout id
4. Installing HS app triggers /install
5. Get tokens for HubSpot
6. Get portal info from the HS token
7. Get the payment made previously via the stripe checkout id
8. Create an account with all details
9. Create a token row with token info
10. TODO: connect payment to account through junction table

## Instantly Webhooks