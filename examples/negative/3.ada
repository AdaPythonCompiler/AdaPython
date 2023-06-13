with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO
procedure Greet is
A : Integer
begin
   if A = 0 
      Put_Line("A is zero");
   elsif A > 0 then
      Put_Line("A is positive");
   elsif A = 1 then
      Put_Line("A is positive");
   else
      Put_Line("A is not zero");
   Put_Line("Hello, world!");
end Greet;
