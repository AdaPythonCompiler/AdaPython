procedure Permute (A : in out Int_Array; L, R : Integer) is
    begin
    if L = R then
        for I in A'Range loop
            Put (A (I), Width => 2);
        New_Line;
    else
        for J in L .. R loop
            Swap (A, L, J);
            Permute (A, L + 1, R);
            Swap (A, L, J);
end Permute;
