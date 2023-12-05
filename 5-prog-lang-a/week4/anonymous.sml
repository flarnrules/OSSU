fun n_times (f,n,x) =
    if n=0
    then x
    else f (n_times (f,n-1,x));

fun triple_n_times (n,x) =
    n_times(let fun triple x = 3*x in triple end,n,x);

fun filter (f,xs) =
    case xs of
	[] => []
      | x::xs' => if f x
		  then x::(filter (f,xs'))
		  else filter (f,xs');

fun is_even v =
    (v mod 2 = 0);

fun all_even xs = filter (is_even, xs);

fun all_even_and xs = filter ((fn (_,v) => is_even v), xs);
