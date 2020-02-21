// Set up constant variables
const TAX_RATE = 1.13;
const ACCESSORY_PRICE = 9.99;
const PHONE_PRICE = 399.99;
const SPENDING_THRESHOLD = 999.99;


var bank_account_balance = 3000.00;

var purchase_amount = () => {
    var total_amount = 0.00;
    while (final_price_with_tax(total_amount + PHONE_PRICE) < bank_account_balance ) {
        total_amount += PHONE_PRICE;
        if (total_amount < SPENDING_THRESHOLD) {
            total_amount += ACCESSORY_PRICE;
        }
    }
    return total_amount
}


var final_price_with_tax = (purchase_amount) => {
    return purchase_amount * TAX_RATE;
};

var display_final_price = (purchase_amount) => {
    return "Final Price: $" + purchase_amount.toFixed(2)
}

var display_remaining_fund = () => {
    return "Fund Remaining: $" + bank_account_balance.toFixed(2)
}

var make_purchase_and_display_purchase_detail = () => {
    const final_price = final_price_with_tax(purchase_amount());
    if (final_price < bank_account_balance) {
        console.log(display_final_price(final_price));
        // Make the purchase
        bank_account_balance -= final_price;
        console.log(display_remaining_fund());
    }
}

console.log(purchase_amount())
console.log(final_price_with_tax(purchase_amount()))

make_purchase_and_display_purchase_detail();