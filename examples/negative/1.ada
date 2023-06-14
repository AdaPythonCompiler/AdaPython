procedure Cos
   A : Int_Arra
   type Int_Array is of Integer
   procedure Swap (A : in out Int_Array; I, J : Integer) is
      T : Integer := A (I);
   begin
      A (I) := A (J);
      A (J) := T;
   end Swap;
end Cos;