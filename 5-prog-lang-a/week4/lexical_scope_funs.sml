(* lexical scope *)
(* example 1 *)
val x = 1;

fun f y =
    let
	val x = y + 1
    in
	fn z => x + y + z
    end;

val x = 3; (* irrelevant *)
val g = f 4; (* call f with 4, returns function that adds 9 *)
val y = 5; (* irrelevant *)
val z = g 6; (* get 15 because 9+6 *)

(* example 2 *)
fun f g =
    let
	val x = 3
    in
	g 2
    end;

val x = 4;
fun h y = x + y; (* add 4 to its argument *)
val z = f h;

(* example 3 *)
fun f1 y =
    let
	val x = y + 1
    in
	fn z => x + y + z
    end;

fun f2 y =
    let
	val q = y + 1
    in
	fn z => q + y + z
    end;

val x = 17;
val a1 = (f1 7) 4;
val a2 = (f2 7) 4;

(* example 4 *)
fun filter (f, xs) =
    case xs of
	[] => []
      | x::xs' => if f x then x::(filter(f,xs')) else filter(f, xs');

fun greaterThanX x = fn y => y > x;
fun noNegatives xs = filter(greaterThanX ~1, xs);
fun allGreater (xs,n) = filter (fn x => x > n, xs);

		  



