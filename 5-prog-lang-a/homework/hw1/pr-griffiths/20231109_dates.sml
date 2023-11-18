(*1*)
fun is_older (date1: int * int * int, date2: int * int * int) =
    (#1 date1 * 365 + #2 date1 * 31 + #3 date1) < (#1 date2 * 365 + #2 date2 * 31 + #3 date2)
   

(*2*)						      
fun number_in_month (xs : (int * int * int) list, n : int) =
    if null xs
    then 0
    else if #2 (hd xs)=n
    then 1 + number_in_month(tl xs, n)
    else number_in_month(tl xs, n)

			
(*3*)			
fun number_in_months (lod : (int * int * int) list, ys : int list) = 
    if null ys
    then 0
    else number_in_months(lod, tl ys) + number_in_month(lod, hd ys)

(*4*)
fun dates_in_month (dates : (int * int * int) list, month : int) = 
	if null dates
	then []
	else if #2 (hd dates)=month
	then hd dates:: dates_in_month(tl dates, month)
	else dates_in_month(tl dates, month)


(*5*)			   
fun dates_in_months (lod : (int * int * int)list, lom : int list) =
    if null lom
    then []
    else dates_in_month(lod, hd lom)@dates_in_months(lod, tl lom)     (* @ is the list-append operator in ML*)


(*6*)						    
fun get_nth (words : string list, n : int) =	
    if null words
    then hd words
    else
	let fun count (from:int, words : string list) =
	    if from=n
	    then hd words
	    else count (from+1, tl words)
	in
	    count (1, words)
	end						    


(*7*)

fun date_to_string (date: int * int * int) =
    let
	val month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    in
	get_nth (month, #2 date)^" "^Int.toString (#3 date)^", "^Int.toString (#1 date)
    end	    


(*8 continue here*)	
fun number_before_reaching_sum (sum : int, numbers : int list) =
    if null numbers
    then 0
    else
	let
	    fun sum_list(total : int, numbers :int list) =
		if total >= sum
		then 0
		else 1 + sum_list(total + (hd numbers), tl numbers)
	in
	    sum_list(hd numbers, tl numbers)
	end

(*9*)
fun what_month(day : int) =
    1 + number_before_reaching_sum(day,[31,28,31,30,31,30,31,31,30,31,30,31])
				

(*10*)
				  
fun month_range(day1 :int, day2:int) =
    if day1 > day2
    then []
	     
    else what_month(day1) :: month_range(day1+1, day2)


(*11*)

					
