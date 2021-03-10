                    (* types and modules *)
type symbol = string 

module Symbols = Set.Make (struct
  type t = symbol
  let compare = compare
end);;

module Model = Map.Make (struct
  type t = symbol
  let compare = compare
end);;

type sentence = Symbol of symbol
                | Not of sentence
                | And of sentence list
                | Or of sentence list
                | Implication of sentence * sentence
                | Biconditional of sentence * sentence
             
type knowledge = sentence               (* And type *)   
type query = sentence                  (* Symbol type *)

module Printer = struct
  let rec sentence_to_str : sentence -> string
    = fun sentence ->
    match sentence with
    |Symbol s -> s
    |Not s -> "~"^(sentence_to_str s)
    |And l -> l_to_str l " && "
    |Or l -> l_to_str l " ||  "
    |Implication (s1,s2) -> (sentence_to_str s1)^" -> "^(sentence_to_str s2)
    |Biconditional (s1,s2) -> (sentence_to_str s1)^" <-> "^(sentence_to_str s2)
  
  and l_to_str l op = 
    let rec aux l op acc =
      match l with
      |[] -> acc^" )"
      |[x]-> acc^(sentence_to_str x)^" )"
      |hd::tl -> aux tl op (acc^(sentence_to_str hd)^op)
    in aux l op "( "   
    
  let symbols_to_str : Symbols.t -> string
  = fun symbols -> (Symbols.fold (fun x a -> a^x^", ") symbols "{ ")^"}"

  let model_to_str : 'a Model.t -> string
  = fun model -> (Model.fold (fun k d a -> a^k^":"^(string_of_bool d)^", ") model "{ ")^"}"

  let print_sentence s = print_endline (sentence_to_str s)
  let print_symbols s = print_endline (symbols_to_str s)
  let print_model m = print_endline (model_to_str m)
end


                    (* 주요 함수들 *)
let add : sentence -> sentence -> sentence             (* And type -> And type *)  
= fun s1 s2 -> 
  match s1 with
  | And l -> And (s2::l)
  | _ -> raise (Failure "you cannot add. invalidate knowledge.")


let all_symbols : sentence -> Symbols.t
= fun sent ->
  let rec aux : sentence -> Symbols.t -> Symbols.t 
  = fun sent acc-> 
 match sent with
 |Symbol s -> Symbols.union acc (Symbols.singleton s) 
 |Not s -> aux s acc
 |And l | Or l -> List.fold_left (fun a x -> aux x a) acc l
 |Implication (s1, s2) | Biconditional (s1, s2) -> aux s2 (aux s1 acc) 
  in aux sent Symbols.empty
  

let rec evaluate : sentence -> 'a Model.t -> bool
 = fun sentence model ->
    match sentence with
    | Symbol symbol -> (try Model.find symbol model 
                       with err -> raise (Failure ("variable"^symbol^"not in model.")))                 
    | Not s -> not (evaluate s model)
    | And l -> List.for_all (fun s -> evaluate s model) l  
    | Or l -> List.exists (fun s -> evaluate s model) l 
    | Implication (s1, s2) -> not (evaluate s1 model) || (evaluate s2 model)
    | Biconditional (s1, s2) -> let eval_s1, eval_s2 = evaluate s1 model , evaluate s2 model in
                                (eval_s1 && eval_s2) || (not eval_s1 && not eval_s2)               


let model_check : knowledge -> query -> bool  
  = fun k q ->
  let symbols = let set = Symbols.union (all_symbols k) (all_symbols q) in
                Symbols.fold (fun x a -> x::a) set []      (* convert set to list *)
  in               
  let rec check_all : knowledge -> query -> symbol list -> 'a Model.t-> bool
    = fun k q s m ->
      match s with
      |[] -> let (eval_k , eval_q) = (evaluate k m, evaluate q m ) in
             not eval_k || eval_q
      |hd::tl -> let (m1, m2) = (Model.add hd true m, Model.add hd false m) in
                  (check_all k q tl m1) && (check_all k q tl m2)
  in (check_all k q symbols Model.empty)        
             
