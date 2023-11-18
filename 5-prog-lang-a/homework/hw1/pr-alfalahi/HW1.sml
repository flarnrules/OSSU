fun is_older (d1 : int*int*int, d2 : int*int*int) = 
    if d1 = d2
    then false
    else if #1 d1 < #1 d2
    then true
    else if #1 d1 = #1 d2 andalso #2 d1 < #2 d2
    then true
    else if #1 d1 = #1 d2 andalso #2 d1 = #2 d2 andalso #3 d1 < #3 d2
    then true
    else false;


fun number_in_month (d_list : (int*int*int) list, month : int)=
    if null d_list
    then 0
    else  if #2 (hd d_list) = month
    then 1 + number_in_month (tl d_list, month)
    else number_in_month (tl d_list, month);


(*fun  number_in_months (d_list : (int*int*int) list, months_list : int list)=
     if null months_list
     then 0
     else number_in_month (d_list, hd month_list)
	  + number_in_months (d_list, tl month_list); *)


fun dates_in_month (d_list : (int*int*int) list, month : int)=
    if null d_list 
    then []
    else if #2 (hd d_list) = month
    then hd d_list :: dates_in_month (tl d_list, month)	   
    else dates_in_month (tl d_list, month);

fun dates_in_months (d_list :(int*int*int) list, month_list : int list)=
    if null month_list
    then []
    else dates_in_month (d_list, hd month_list)
	 @ dates_in_months (d_list, tl month_list);

fun get_nth (strings : string list, n : int)=
    if n = 1
    then hd strings
    else get_nth (tl strings, n-1)
			 
fun date_to_string (d : int*int*int)=
    let val  months =["January","February", "March", "April", "May", "June", "July",
		 "August", "September", "October", "November", "December"]
    in
	get_nth (months, #2 d)^ " " ^  Int.toString (#3 d) ^ ", " ^ Int.toString (#1 d)
    end;

fun number_before_reaching_sum (sum : int, l : int list)=
    if sum <= 0
    then ~1
    else 1 + number_before_reaching_sum ((sum - hd l), tl l)
			    
fun what_month (day : int) =
    let val months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in  number_before_reaching_sum (day, months_days) + 1
    end;

fun  month_range (day1 : int, day2 : int)=
     if day1 > day2
     then []
     else what_month (day1) :: month_range ((day1+1), day2);

fun oldest (d_list)=
    if null d_list
    then NONE
    else let fun oldest_not_empty(d_list)=
		 if null (tl d_list)
		 then hd d_list
		 else let val oldest_val= oldest_not_empty(tl d_list)
		      in if is_older(hd d_list, oldest_val)
			 then hd d_list
			 else oldest_val
		      end
	 in SOME (oldest_not_empty(d_list))
	 end;


fun  number_in_months_challenge (d_list : (int*int*int) list, month_list : int list)=
     if month_list = []
     then 0
     else let
	 fun in_list (m : int, i_list : int list)=
	     if null i_list
	     then false
	     else if m = hd i_list
	     then true
	     else in_list(m, (tl i_list))
	     
	 fun remove_dublicat (i_list : int list) =
		  if null i_list
		  then []
		  else if in_list(hd i_list, tl i_list)
		  then remove_dublicat(tl i_list)
		  else (hd i_list) :: remove_dublicat(tl i_list)
	 val new_month_list = remove_dublicat(month_list)
     in
	 number_in_months (d_list, new_month_list)
     end;


fun dates_in_months_challenge (d_list :(int*int*int) list, month_list : int list)=
    if month_list = []
    then []
    else  let
	fun in_list (m : int, i_list : int list)=
	    if null i_list
	    then false
	    else if m = hd i_list
	    then true
	    else in_list(m, (tl i_list))
			
	fun remove_dublicat (i_list : int list) =
	    if null i_list
	    then []
	    else if in_list(hd i_list, tl i_list)
	    then remove_dublicat(tl i_list)
	    else (hd i_list) :: remove_dublicat(tl i_list)
	val new_month_list = remove_dublicat(month_list)
    in
	dates_in_months (d_list, new_month_list)
    end;


fun reasonable_date (date : int*int*int) =
    if #1 date <= 0
    then false
    else let
	val months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
	fun return_i (l : int list, i : int) = if i = 1 then hd l else return_i (tl l, i-1)
	fun real_month (m : int) = if m > 0 andalso m <= 12 then true else false
	fun real_day (day : int, month :int) = if return_i(months_days, month) >= day andalso day > 0
					       then true
					       else false  
	fun is_leap_year (year : int) = if year mod 400 = 0 orelse
					   (year mod 4 = 0 andalso year mod 100 <> 0)
					then true
					else false
    in
	if is_leap_year (#1 date) andalso #2 date = 2 
	then if real_month(#2 date) andalso real_day(#3 date , 13) then true else false
	else if real_month(#2 date) andalso real_day(#3 date , #2 date) then true else false
    end;

