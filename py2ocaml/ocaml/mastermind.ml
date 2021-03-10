open Logic

let colors = ["red" ; "blue" ; "green" ; "yellow"]
let color_with_pos color = List.map (fun n -> Symbol (color^n) ) ["0";"1";"2";"3"]
let pos_with_colors pos = List.map (fun c -> Symbol (c^pos)) colors

let symbols = List.flatten (List.map pos_with_colors ["0";"1";"2";"3"])

let create_all_impl_pairs l = 
  let rec aux l front = 
    match l with
    |head::tail -> let target =  List.map ( fun x -> Implication (head, Not x) ) (front@tail) 
                   in target @ (aux tail (front@[head])) 
    |[] -> []
  in And (aux l [])

let knowledge0 = And []
let knowledge1 = List.fold_left (fun k color -> add k (Or (color_with_pos color)) ) knowledge0 colors
let knowledge2 = List.fold_left (fun k color -> add k (create_all_impl_pairs (color_with_pos color))) knowledge1 colors
let knowledge3 = List.fold_left (fun k pos -> add k (create_all_impl_pairs (pos_with_colors pos))) knowledge2 ["0";"1";"2";"3"]

let knowledge4 = add knowledge3 ( Or [ And[Symbol("red0"); Symbol("blue1"); Not(Symbol("green2")); Not(Symbol("yellow3"))];
                                        And[Symbol("red0"); Symbol("green2"); Not(Symbol("blue1")); Not(Symbol("yellow3"))];
                                        And[Symbol("red0"); Symbol("yellow3"); Not(Symbol("blue1")); Not(Symbol("green2"))];
                                        And[Symbol("blue1"); Symbol("green2"); Not(Symbol("red0")); Not(Symbol("yellow3"))];
                                        And[Symbol("blue1"); Symbol("yellow3"); Not(Symbol("red0")); Not(Symbol("green2"))];
                                        And[Symbol("green2"); Symbol("yellow3"); Not(Symbol("red0")); Not(Symbol("blue1"))] ] )

let knowledge5 = add knowledge4 ( And[Not(Symbol("blue0"));Not(Symbol("red1"));Not(Symbol("green2"));Not(Symbol("yellow3"))]  );;                                      

let main () = List.iter (fun symbol -> if model_check knowledge5 symbol then Printer.print_sentence symbol else ()) symbols 
in main ()