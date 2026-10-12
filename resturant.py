from concurrent.futures import ProcessPoolExecutor
import time
#customer resturant price negotiation
#remembering customers and their negotiated price (relation)
#base model fee to the platform based on yearly sales assigning them to a slab
def resturant_renegotiate(current_price):
	return current_price
def customer_renegotiate(current_price):
	return current_price
def negotiate(resturant_min,customer_max,rider_fare_pay):
	resturant_acceptable=resturant_min
	customer_acceptable=customer_max

	start_time=time.time()

	while True:
		with ProcessPoolExecutor() as executor:
			f1=executor.submit(resturant_renegotiate)
			f2=executor.submit(customer_renegotiate)

			result1=f1.result()
			result2=f2.result()
		if resturant_acceptable+customer_acceptable