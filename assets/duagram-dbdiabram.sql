//// -- LEVEL 1
//// -- Tables and References

// Creating tables
Table Jobs as J {
  id int [pk, increment] // auto-increment
  full_name varchar
  created_at timestam
}

Table Countries {
  code int [pk]
  name varchar
  continent_name varchar
 }

Table Senority {
  code int [pk]
  name varchar
  experience_range_min int
  experience_range_max int
}

Table Period_evaluation {
  id int [pk, increment]
  name varchar
}

Table Salaries as S {
  id int [pk, increment]
  job int 
  country int
  senority int 
  period_input int
  Salary double
  
}

// Creating references
// You can also define relaionship separately
// > many-to-one; < one-to-many; - one-to-one
Ref: S.job > Jobs.id  
Ref: S.country > Countries.code  
Ref: S.senority > Senority.code  
Ref: S.period_input > Period_evaluation.id  
//Ref: S.Job > Countries.code  
//Ref: merchants.country_code > countries.code