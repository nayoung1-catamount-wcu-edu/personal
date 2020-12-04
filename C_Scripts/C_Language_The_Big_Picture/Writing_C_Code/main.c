#include <stdio.h>
// #include "orders.h"

int main(int argc, char *argv[])
{
	int nums1[5] = { 1, 2, 3, 4, 5 };

	int *nums2 = nums1;

	printf("nums1 --> %p\n", nums1);
	printf("nums2 --> %p\n\n", nums2);

	nums2 += 2;

	printf("nums1 --> %p\n", nums1);
	printf("nums2 --> %p\n\n", nums2);

	*nums2 = 100;

	for (int i = 0; i < 5; i++)
		printf("%d ", nums1[i]);

	//-----------------------------------

	//char *name1 = "Brice";
	
	//printf("%s\n\n", name1);

	//char *name2 = name1;

	//printf("name1 --> %p\n", name1);
	//printf("name2 --> %p\n\n", name2);

	//name2 += 2;

	//printf("name1 --> %p\n", name1);
	//printf("name2 --> %p\n\n", name2);

	//*name2 = 'y';

	//printf("%s\n", name1);
	
	//-----------------------------------
	
	//double order_subtotal = 50.00;

	//double grand_total = calculate_order_total(order_subtotal);

	//printf("Grand total: %lf", grand_total);
}