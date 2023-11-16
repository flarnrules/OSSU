(* Programming Languages Part A - Homework 1 - Date Functions *)
(* Assignment by Benjamin Reifenberg, November 2023 *)

(* Function 1 - is_older *)
fun is_older ((year1, month1, day1) : int*int*int, (year2, month2, day2) : int*int*int) =
    if year1 < year2
    then true
    else if year1 = year2 andalso month1 < month2
    then true
    else if month1 = month2 andalso day1 < day2
    then true
    else false;

(* Function 2 - number_in_month *)
(* this will require recursion *)
fun number_in_month (dates : (int*int*int) list, month : int) =
    let
	fun months(dates) =
	    if null dates
	    then []
	    else
		let
		    val date : int * int * int = hd dates
		in
		    #2 date :: months (tl dates)
		end
	fun count (ms, targetMonth) =
	    if null ms
	    then 0
	    else
		if hd ms = targetMonth
		then 1 + count (tl ms,targetMonth)
		else count (tl ms, targetMonth)
    in
	count (months dates, month)
    end;

(* Function 3 - number_in_months *)
(* use function 2 *)
fun number_in_months (dates : (int*int*int) list, months : int list) =
    if null months
    then 0
    else number_in_month(dates, hd months) + number_in_months(dates, tl months);

(* Function 4 - dates_in_month *)
fun dates_in_month (dates : (int*int*int) list, month: int) =
    let
	fun filter_dates(dates, month) =
	    if null dates then
		[]
	    else
		let
		    val thisDate : int * int * int = hd dates
		    val restDates = tl dates
		in
		    if #2 thisDate = month then
			thisDate :: filter_dates(restDates, month)
		    else
			filter_dates(restDates, month)
		end
    in
	filter_dates(dates, month)
    end;

(* Function 5 - dates_in_months *)
fun dates_in_months (dates : (int*int*int) list, months: int list) =
    if null months then
	[]
    else
	dates_in_month(dates, hd months) @ dates_in_months(dates, tl months);


(* Function 6 - get_nth *)
fun get_nth (strs: string list, n: int) =
    if n = 1 then hd strs
    else get_nth (tl strs, n - 1);

(* Function 7 - date_to_string *)
fun date_to_string ((year, month, day) : int * int * int) =
    let
        val months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        val monthString = get_nth(months, month)
    in
        monthString ^ " " ^ Int.toString(day) ^ ", " ^ Int.toString(year)
    end;

(* Function 8 - number_before_reaching_sum *)
fun number_before_reaching_sum (targetSum : int, numbers : int list) =
    let
        fun acc_sum (acc, nums, count) =
            if acc + hd nums >= targetSum then
                count + 1
            else
                acc_sum (acc + hd nums, tl nums, count + 1)
    in
        acc_sum (0, numbers, 0)
    end;

(* Function 9 - what_month *)
fun what_month (dayOfYear : int) =
    let
        val daysInMonths = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        fun find_month (daysList, month) =
            if dayOfYear <= hd daysList then
                month
            else
                find_month (tl daysList, month + 1)
    in
        find_month (daysInMonths, 1)
    end;

(* Function 10 - month_range, doesn't work *)
fun month_range (day1 : int, day2 : int) =
    let
        fun build_range (currentDay, endDay, acc) =
            if currentDay > endDay then acc
            else build_range (currentDay + 1, endDay, acc @ [what_month currentDay])
    in
        build_range (day1, day2, [])
    end;

(* Function 11 - oldest *)
fun oldest (dates : (int * int * int) list) : (int * int * int) option =
    let
        fun is_older ((y1, m1, d1), (y2, m2, d2)) =
            y1 < y2 orelse (y1 = y2 andalso (m1 < m2 orelse (m1 = m2 andalso d1 < d2)))
        fun find_oldest (currentOldest, remainingDates) =
            if null remainingDates then
                currentOldest
            else
                if isSome currentOldest then
                    let
                        val thisDate = hd remainingDates
                        val nextOldest = if is_older (thisDate, valOf currentOldest)
                                         then SOME thisDate
                                         else currentOldest
                    in
                        find_oldest (nextOldest, tl remainingDates)
                    end
                else
                    find_oldest (SOME (hd remainingDates), tl remainingDates)
    in
        find_oldest (NONE, dates)
    end;
