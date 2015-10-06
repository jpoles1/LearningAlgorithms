primes :: [Int]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
main :: IO()
main = print $ binSearch 0 (length primes-1) 61 primes
primeSearch :: Int -> Maybe Int
primeSearch targ = binSearch 0 (length primes-1) targ primes
binSearch :: (Ord a) => Int -> Int -> a -> [a] -> Maybe Int
binSearch mini maxi target arr
  | mini > maxi = Nothing
  | guess == target = Just guessindex
  | guess < target = binSearch (guessindex+1) maxi target arr
  | guess > target = binSearch mini (guessindex-1) target arr
  | otherwise = undefined
  where
    guessindex = quot (mini+maxi) 2
    guess = arr !! guessindex
