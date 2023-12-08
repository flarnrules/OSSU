(* a set of ints with three operaions *)

datatype set = s of { insert : int -> set,
		      member : int -> bool,
		      size   : unit -> int };


(* datatype set = s of { insert : int -> set,
		      member : int -> bool,
		      size   : unit -> int }; *)

(* val empty_set : set *)


(* example client *)
fun use_sets () = (* unit -> int *)
    let val S s1 = empty_set
	val S s2 = (#insert s1) 34
	val S s3 = (#insert s2) 34
	val S s4 = #insert s3 19
    in
	if (#member s4) 42
	then 99
	else if (#member s4) 19
	then 17 + (#size s3) ()
	else 0
    end;

