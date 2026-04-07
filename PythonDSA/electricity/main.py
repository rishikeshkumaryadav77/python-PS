function calculateBill(units) {
    if (units < 0) return "Invalid input";

    let bill = 0;

    bill += Math.min(units, 100) * 5;

    if (units > 100) {
        bill += Math.min(units - 100, 100) * 7;
    }

    if (units > 200) {
        bill += (units - 200) * 10;
    }

    return bill;
}