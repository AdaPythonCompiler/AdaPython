with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;


procedure Greet is
A : Integer;
begin
   if A = 0 then
      Put_Line("A is zero");
   elsif A > 0 then
      Put_Line("A is positive");
   else
      Put_Line("A is not zero");
   end if;
   Put_Line("Hello, world!");
end Greet;

procedure Main is
   I : Integer := 1;
begin
   while I <= 10 loop
      Put_Line("Hello, world!");
      I := I + 1;
   end loop;
   Put_Line("Hello, world!");
end Main;
