double calculate_sales_tax(double order_subtotal)
{
	return order_subtotal * .05; // 5% sales tax
}

double calculate_shipping_cost(double order_subtotal)
{
	return order_subtotal * .1; // 10% shipping charge
}

double calculate_order_total(double order_subtotal)
{
	double order_total = order_subtotal + calculate_sales_tax(order_subtotal);
	order_total += calculate_shipping_cost(order_subtotal);
	return order_total;
}