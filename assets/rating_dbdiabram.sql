//// -- LEVEL 1
//// -- Tables and References

// Creating tables
Table Industries{
  id int [pk, increment]
  name varchar
  description varchar
}
 
Table  Companies as C {
  id int [pk, increment] // auto-increment
  industry_id int
  full_name varchar
  created_at timestamp
  description varchar
}

Table Company_locations {
  Id_location int [pk, increment]
  company_id int
  country_code int
  location varchar
}

Table Countries {
  code int [pk]
  name varchar
  continent_name varchar
 }
 
 
Table Reviews {
  id_review int [pk, increment]
  company_id int
  title varchar
  position varchar
  score int
  review_date timestamp
  useful int
 }

Table Pros{
  id_pro int [pk,increment]
  review_id int
  pro_description varchar
}

Table Cons{
  id_con int [pk,increment]
  review_id int
  con_description varchar
}

Table Interviews {
  id_interview int [pk, increment]
  company_id int
  difficult int
  description varchar
  experience int
  review_date timestamp
  offer_recived boolean
 }


// Creating references
// You can also define relaionship separately
// > many-to-one; < one-to-many; - one-to-one
Ref: C.industry_id < Industries.id 
Ref: C.id > Company_locations.company_id 
Ref: Company_locations.country_code > Countries.code
Ref: Reviews.company_id > Companies.id
Ref: Pros.review_id > Reviews.id_review
Ref: Cons.review_id > Reviews.id_review
Ref: Interviews.company_id > Companies.id
//Ref: S.Job > Countries.code  
//Ref: merchants.country_code > countries.code

//Ref: "Countries"."name" < "Company_locations"."location"


