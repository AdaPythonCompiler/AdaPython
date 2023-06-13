procedure Main is
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
end Main;