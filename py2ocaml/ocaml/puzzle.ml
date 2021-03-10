open Logic

let people = ["Gilderoy" ; "Pomona" ; "Minerva" ; "Horace"]
let houses = ["Gryffindor" ; "Hufflepuff" ; "Ravenclaw" ; "Slytherin"]

let one_person_symbols person = List.map (fun house-> Symbol (person^house)) houses
let one_house_symbols house = List.map (fun person-> Symbol (person^house)) people

let symbols = List.flatten (List.map one_person_symbols people);;

let create_all_impl_pairs l = 
  let rec aux l front = 
    match l with
    |head::tail -> let target =  List.map ( fun x -> Implication (head, Not x) ) (front@tail) 
                   in target @ (aux tail (front@[head])) 
    |[] -> []
  in And (aux l [])

let knowledge0 = And [] 
let knowledge1 = List.fold_left (fun k person -> add k (Or (one_person_symbols person)) ) knowledge0 people
let knowledge2 = List.fold_left (fun k person -> add k (create_all_impl_pairs (one_person_symbols person))) knowledge1 people
let knowledge3 = List.fold_left (fun k house -> add k (create_all_impl_pairs (one_house_symbols house))) knowledge2 houses

let knowledge4 = add knowledge3 (Or[Symbol("GilderoyGryffindor"); Symbol("GilderoyRavenclaw")])
let knowledge5 = add knowledge4 ( Not(Symbol("PomonaSlytherin")) )
let knowledge6 = add knowledge5 ( Symbol("MinervaGryffindor") );;

let main () = List.iter (fun symbol -> if model_check knowledge6 symbol then Printer.print_sentence symbol else ()) symbols 
in main ()
  
  
  
