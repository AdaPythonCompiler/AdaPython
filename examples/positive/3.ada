procedure Main is
   type Int_Array is array (Integer range <>) of Integer;
   procedure Swap (A : in out Int_Array; I, J : Integer) is
      T : Integer := A (I);
   begin
      A (I) := A (J);
      A (J) := T;
   end Swap;
 
   procedure Permute (A : in out Int_Array; L, R : Integer) is
   begin
      if L = R then
         for I in A'Range loop
            Put (A (I), Width => 2);
         end loop;
         New_Line;
      else
         for J in L .. R loop
            Swap (A, L, J);
            Permute (A, L + 1, R);
            Swap (A, L, J);
         end loop;
      end if;
   end Permute;
 
   N : Integer;
   A : Int_Array (1 .. 10);
end Main;