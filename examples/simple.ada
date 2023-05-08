with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;


procedure Greet is
A : Integer;
begin
   if A = 0 then
      Put_Line("A is zero");
   elsif A > 0 then
      Put_Line("A is positive");
   elsif A = 1 then
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

procedure MainFor is
begin
   for I in 1 .. 10 loop
      Put_Line("Hello, world!");
   end loop;
   Put_Line("Hello, world!");
end MainFor;

procedure MainCase is
   I : Integer := 1;
begin
   case I is
      when 1 =>
         Put_Line("I is 1");
      when 2 =>
         Put_Line("I is 2");
      when 3 =>
         Put_Line("I is 3");
      when others =>
         Put_Line("I is others");
   end case;
end MainCase;