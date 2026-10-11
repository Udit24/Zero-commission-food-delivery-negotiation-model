def rider_fare_pay(base_fare, distance,time,demand,availability,vote_count):
	distance_pay=distance*1.5
	time_pay=time*0.25
	surge_multiplier=demand/max(availability,1)
	vote_bonus=vote_count*0.10
	total_pay=(base_fare+distance+time_pay)*surge_multiplier+vote_bonus
	return round(total_pay,2)
print(f"RIder Payout: ₹{rider_fare_pay(3.00,5,15,10,8,5)}")