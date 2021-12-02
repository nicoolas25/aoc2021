puts ARGF.
  each_line.
  map(&:to_i).
  each_cons(3).
  map(&:sum).
  each_cons(2).
  count { |a, b| b > a }
