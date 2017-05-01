function [polyX, indices] = multinom2(X,degree)
     
    [m,n] = size(X);
    
    if(degree == 1)
         
        polyX = X;
        indices = zeros(n,1);
 
    else
        polyX = [];
        [remaining_PolyX prev_indices] = multinom(X,degree-1);
 
        if(prev_indices(1) == 0)
            offset = 0;
            for i = 1:numel(prev_indices)
                prev_indices(i) = n-offset;
                offset = offset + 1;
            end
        else
            for i = 1:numel(prev_indices)
                total = 0;
                for j = i:numel(prev_indices)
                    total = total + prev_indices(j);
                end
                prev_indices(i) = total;
            end
        endif
 
        for i = 1:n
            feature = X(:,i);
            for j = 0:(prev_indices(i)-1)
                polyX = [polyX X(:,i).*remaining_PolyX(:,size(remaining_PolyX,2)-j)];
            end
        end
 
        indices = prev_indices;
 
    endif
 
end
