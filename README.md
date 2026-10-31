# 69 bài tập Python và thuật toán — kiến thức và cách làm

Tài liệu ôn tập chia theo 13 nhóm. Mỗi nhóm có kiến thức Python cần dùng, các chú ý khi code và hướng giải cho từng bài. Nhấn vào tên bài để mở đề gốc trên [Lập Trình Online](https://laptrinhonline.club/).

Cắt thanh kim loại đã được bỏ khỏi phạm vi ôn theo yêu cầu; danh sách còn 69 bài. Số thứ tự 1–69 của các bài còn lại được giữ nguyên để khớp các file bài tập hiện có. Đây là tài liệu hướng dẫn, không phải xác nhận rằng mọi bài đã được tự làm lại độc lập.

## Mục lục

- [Kiến thức Python dùng chung](#kien-thuc-chung)
- [I. Cơ bản, xử lý chuỗi và số nguyên lớn](#nhom-i)
- [II. Duyệt dãy, ma trận và điều kiện](#nhom-ii)
- [III. Số học, quy luật và ngày tháng](#nhom-iii)
- [IV. Phương trình và hình học](#nhom-iv)
- [V. Dictionary: tra cứu, tần suất và tổng hợp](#nhom-v)
- [VI. Sắp xếp và xử lý bản ghi](#nhom-vi)
- [VII. Đệ quy và quay lui](#nhom-vii)
- [VIII. Stack và mô phỏng hàng vòng tròn](#nhom-viii)
- [IX. Đoạn liên tục: set, tổng tích lũy và cửa sổ](#nhom-ix)
- [X. BFS/DFS, trạng thái và nhóm liên thông](#nhom-x)
- [XI. Heap và tham lam](#nhom-xi)
- [XII. Quy hoạch động](#nhom-xii)
- [XIII. Cây khung nhỏ nhất và DSU](#nhom-xiii)

<a id="kien-thuc-chung"></a>
## Kiến thức Python dùng chung

### Nhập và xuất

```python
from sys import stdin
input = stdin.readline

n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
s = input().rstrip("\n")

print(*arr)
print(f"{3.14159:.3f}")
```

- `readline()` giữ ký tự xuống dòng. Dùng `rstrip("\n")` khi cần giữ khoảng trắng đầu/cuối; dùng `strip()` khi những khoảng trắng đó không thuộc dữ liệu.
- `int(input())` và `input().split()` đã xử lý khoảng trắng thích hợp khi đọc số, không cần thêm `strip()`.
- Đọc đến EOF bằng `for line in stdin`. Chỉ dùng cách này nếu đề không có số lượng dòng/test ở đầu.
- Nếu cần xử lý từng số, có thể duyệt trực tiếp `for x in map(int, input().split())` để tránh giữ thêm một list số nguyên.
- `input = stdin.readline` giảm chi phí nhập; thuật toán quá chậm vẫn cần được sửa.
- In đúng thứ tự, số chữ số thập phân, khoảng trắng và thông báo theo đề. Bỏ các dòng in dùng để debug trước khi nộp.

### Thao tác nền tảng

- `/` là chia thực; `//` là chia nguyên; `%` lấy dư; `**` là lũy thừa. `^` không phải lũy thừa trong Python.
- List lưu dãy có thứ tự; tuple phù hợp cho bản ghi/trạng thái; set lưu giá trị phân biệt; dict ánh xạ khóa tới dữ liệu.
- List đánh chỉ số từ `0`. `arr[l:r]` lấy từ `l` đến `r-1` và tạo một list mới.
- `arr.sort()`, `arr.reverse()` và `heapq.heapify(arr)` sửa tại chỗ, trả `None`; không gán kết quả của chúng trở lại `arr`.
- `sorted(arr)` tạo list mới. Set không bảo đảm thứ tự tăng dần; cần `sorted(...)` khi đề yêu cầu.
- Trước khi code, xác định dữ liệu cần lưu, cách cập nhật và điều kiện dừng. Sau đó kiểm tra ví dụ cùng trường hợp biên phù hợp.

<a id="nhom-i"></a>
## I. Cơ bản, xử lý chuỗi và số nguyên lớn

### Python cần ôn

- `int`, `float`, phép toán, vòng `for`, `range` và biến tích lũy.
- Chuỗi bất biến; đảo bằng `s[::-1]`, tách từ bằng `split()`, ghép bằng `" ".join(words)`.
- `int` của Python xử lý số nguyên lớn; không chuyển số nguyên lớn sang `float` để tính toán chính xác.
- `print(*arr)`, f-string và đọc đến EOF.

### Chú ý chung

- Phân biệt đảo ký tự với đảo thứ tự từ.
- Biến tích khởi tạo bằng `1`, biến tổng bằng `0`.
- Với các bài đã chọn giải bằng Python, dùng `int` và thao tác chuỗi theo hướng đang học; không cần thêm kiến thức con trỏ C/C++ để thực hành các cách giải dưới đây.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 1 | [Bài 2.2. Chuyển đơn vị đo C và F](https://laptrinhonline.club/problem/0008dayc) | Phép toán, `float`, f-string | Đọc C, tính `F = C * 9 / 5 + 32`, in `f"{F:.2f}"`. Dùng `/`, không dùng `//`. |
| 2 | [0.Đảo mảng ký tự](https://laptrinhonline.club/problem/basic6) | Chuỗi, slicing, `rstrip` | Đọc số ký tự rồi đọc nguyên dòng chuỗi; in `s[::-1]`. Chỉ bỏ newline nếu khoảng trắng là ký tự cần giữ. Thời gian O(n). |
| 3 | [Đảo từ](https://laptrinhonline.club/problem/tichpxdaotu) | `split`, slicing, `join` | Tách thành các từ, đảo thứ tự list từ, ghép lại bằng dấu cách. Không đảo các chữ bên trong từng từ. Thời gian tuyến tính theo độ dài văn bản. |
| 4 | [Factorial of a large number](https://laptrinhonline.club/problem/tichpxgiaithuasolon) | `int`, vòng lặp; tùy chọn `math.factorial` | Khởi tạo `answer = 1`, nhân lần lượt từ `2` đến `n`, in toàn bộ kết quả. Không lấy modulo, không dùng số thực. Có n−1 phép nhân; chi phí mỗi phép tăng khi số có nhiều chữ số. |
| 5 | [Nhân 2 số lớn](https://laptrinhonline.club/problem/tichpxnhansolon) | `int`, đọc hai dòng | Theo lựa chọn giải bằng Python đã dùng: đọc hai số nguyên rồi in `x * y`. Giữ tính toán dạng nguyên; không đưa qua `float`. |
| 6 | [t2r2. Tổng dãy số](https://laptrinhonline.club/problem/tichpxtongdayso) | `stdin`, vòng lặp, modulo | Đọc các số đến EOF, cộng vào `total`; in tổng modulo `1000000007`. Có thể lấy modulo sau mỗi lần cộng. Không đọc nhầm số đầu thành số lượng phần tử. |

<a id="nhom-ii"></a>
## II. Duyệt dãy, ma trận và điều kiện

### Python cần ôn

- `for`, `range`, `if/elif/else`, `all`, `sum`, `min`, `max`.
- Duyệt cặp kề `arr[i], arr[i+1]`; duyệt bộ ba kề bằng chỉ số ở giữa.
- Ma trận dạng list các list: `matrix[row][col]`.
- `math.isqrt` để kiểm tra chính phương của số nguyên không âm.

### Chú ý chung

- Tạo ma trận bằng `[[0] * m for _ in range(n)]`, tránh `[[0] * m] * n` vì các hàng cùng tham chiếu tới một list.
- Kiểm tra biên trước khi truy cập. Chỉ số âm hợp lệ trong Python nhưng có thể sai ý nghĩa của bài.
- Thống nhất chỉ số từ 0 hoặc từ 1; nếu đề dùng từ 1, chuyển ngay sau khi nhập.
- Phân biệt điều kiện nghiêm ngặt `<`, `>` với điều kiện có bằng `<=`, `>=`.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 7 | [Nhà soạn nhạc tài ba](https://laptrinhonline.club/problem/chipheo) | List, duyệt cặp kề, `all` | Kiểm tra toàn bộ 7 cặp kề của dãy 8 số: cùng tăng thì `TANG`, cùng giảm thì `GIAM`, còn lại `KHONGBIET`. Xét thứ tự gốc, không sort dãy để kiểm tra. |
| 8 | [Làm bài tập](https://laptrinhonline.club/problem/cotyey009) | `min`, `max` | Hai khoảng thời gian `[A,B]` và `[C,D]` giao nhau trong `max(0, min(B,D) - max(A,C))` đơn vị thời gian. Hai đầu chạm nhau cho kết quả 0. O(1). |
| 9 | [0.Dãy Fibonacci đơn giản](https://laptrinhonline.club/problem/i1511) | Gán đồng thời, list, `print(*arr)` | Bắt đầu `a,b = 0,1`; lặp N lần: lưu `a`, rồi cập nhật `a,b = b,a+b`. Đề yêu cầu N số đầu, không chỉ số Fibonacci thứ N. O(N). |
| 10 | [Đếm trên dãy số](https://laptrinhonline.club/problem/tichpxdemday) | `%`, `isqrt`, đếm chẵn/lẻ, cặp và bộ ba kề | Tính 5 kết quả: số không chia hết 3; số chính phương; cặp kề có số sau chia hết số trước; cặp cùng chẵn/lẻ; bộ ba kề tăng ngặt. Kiểm tra số chính phương chỉ khi x≥0, và mẫu khác 0 trước `%`. Cặp cùng chẵn/lẻ tính bằng `even*(even-1)//2 + odd*(odd-1)//2`. Có thể làm tổng thể O(n). |
| 11 | [Tính tổng trên dãy số nguyên](https://laptrinhonline.club/problem/tichpxtinhtong) | Biến tổng dồn, vòng lặp | Đề tính tổng tất cả tổng tiền tố. Với mỗi x: `prefix += x`, rồi `answer += prefix`. Tương đương tổng `arr[i] * (n-i)` khi dùng chỉ số 0. O(n), không cần cộng lại từng đoạn. |
| 12 | [Tính chất đơn điệu của dãy số](https://laptrinhonline.club/problem/tichpxdondieu) | `all`, so sánh cặp kề | Kiểm tra dãy bằng nhau trước; sau đó tăng ngặt, giảm ngặt, tăng không ngặt, giảm không ngặt; còn lại không đơn điệu. Thứ tự xét tránh nhận nhầm dãy hằng hoặc tăng ngặt thành tăng không ngặt. In đúng chuỗi thông báo của đề. O(n). |
| 13 | [Các đường chéo song song với đường chéo chính và đường chéo phụ của ma trận](https://laptrinhonline.club/problem/tichpxdccmatran) | Ma trận, chỉ số, dict hoặc list | Với cùng hệ chỉ số, đường chéo chính qua `(u,v)` có `row-col = u-v`; đường chéo phụ có `row+col = u+v`. Tính tổng nhóm thứ nhất và min nhóm thứ hai. Cách quét mỗi truy vấn đã học dùng được ở giới hạn nhỏ; có thể tiền xử lý tổng theo hiệu và min theo tổng trong O(n²), trả mỗi truy vấn O(1). Min khởi tạo từ phần tử thật hoặc `inf`, không khởi tạo tùy tiện bằng 0. |

<a id="nhom-iii"></a>
## III. Số học, quy luật và ngày tháng

### Python cần ôn

- Chia nguyên `//`, lấy dư `%`, `divmod`, vòng lặp giảm dần.
- `math.gcd`, `math.isqrt`; kiểm tra chính phương bằng `r*r == x`.
- Gán đồng thời để cập nhật tử/mẫu hoặc hai số liên tiếp mà không ghi đè dữ liệu cần dùng.
- `datetime.date`, trừ hai ngày và thuộc tính `.days`.
- Đọc số quá dài dưới dạng chuỗi khi chỉ cần độ dài, không chuyển sang `int`.

### Chú ý chung

- Tránh `log` hoặc căn số thực nếu bài cần kết quả nguyên chính xác.
- Xác định rõ đoạn đóng/mở: nhỏ hơn a khác với nhỏ hơn hoặc bằng a; tính ngày có cộng thêm 1 hay không phụ thuộc đề.
- Khi số lượt rất lớn, tìm quy luật để bỏ qua cả khối thay vì mô phỏng từng phần tử.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 14 | [Đổi sang cơ số 3](https://laptrinhonline.club/problem/tichpxdoics3) | `while`, `%`, `//`, list ký tự | Lặp lấy `n % 3`, rồi `n //= 3`; đảo các chữ số thu được. Xử lý 0 riêng nếu xuất hiện. Không xác định bậc bằng `log(n,3)` vì có thể sai ở lũy thừa của 3. |
| 15 | [t2r2. Tích của dãy cấp số cộng](https://laptrinhonline.club/problem/tichpxtichcapsocong) | `range` có bước, tích nguyên | Với k>0, nhân `n, n-k, n-2k,...` khi còn dương; đó là các số không vượt n cùng phần dư với n khi chia k. Khởi tạo tích bằng 1, không nhân thêm 0. Đề có chỗ ghi k không âm nhưng phép chia cho k chỉ có nghĩa khi k>0; không dùng bước lặp bằng 0. |
| 16 | [0.Ước chung lớn nhất, bội chung nhỏ nhất (Cơ bản)](https://laptrinhonline.club/problem/usclnbscnn) | `math.gcd`, `while True`, `break` | Đọc từng cặp tới `0 0`; tính `g = gcd(a,b)`, với a,b dương thì `lcm = a//g*b`. Kiểm tra cặp dừng trước khi chia. Nếu dữ liệu có một số 0, BCNN bằng 0. Không dò từng ước từ 1 đến min(a,b). |
| 17 | [Bài 2.3. Số chia hết lớn nhất](https://laptrinhonline.club/problem/0009dayc) | `//`, nhân số nguyên | Đáp án `((a-1)//b)*b`, vì phải nhỏ hơn a nghiêm ngặt. Ví dụ a=25,b=5 cho 20, không phải 25. Không cần vòng lặp hoặc đổi sang float. |
| 18 | [0.Bội số của 13](https://laptrinhonline.club/problem/i2311) | `min`, `max`, `range`, `%` | Chuẩn hóa hai đầu L≤R; duyệt cả hai đầu `range(L,R+1)`, chỉ cộng x có `x % 13 != 0`. Đề hỏi tổng những số không chia hết cho 13. Miền giá trị nhỏ nên duyệt trực tiếp phù hợp. |
| 19 | [Rút gọn phân số](https://laptrinhonline.club/problem/tichpxrutgonps) | Gán đồng thời, vòng lặp ngược, `gcd` | Đây là phân số liên tục. Bắt đầu `p,q = arr[-1],1`; với từng a từ áp cuối về đầu, cập nhật `p,q = a*p+q,p`. Cuối cùng chia cả p,q cho gcd và in `p/q`. Dùng số nguyên toàn bộ. Ví dụ `[1,2,3]` cho `10/7`. |
| 20 | [Tính số ngày](https://laptrinhonline.club/problem/tichpxsongay) | `datetime.date`, unpacking | Đọc d,m,y của hai ngày; tạo `date(y,m,d)`, lấy `(end-start).days`. Đề tính ngày gửi nhưng không tính ngày rút nên không cộng thêm 1; cùng ngày cho 0. `date` xử lý năm nhuận. |
| 21 | [Vòng lặp](https://laptrinhonline.club/problem/tichpxvonglap) | Chuỗi, `len`, vòng lặp theo khối, `//` | Đọc chuỗi ghép n,n−1,...,1 và lấy độ dài L. Trừ dần các khối 1 chữ số, 2 chữ số,...; khối d chữ số đầy đủ dài `9*10**(d-1)*d`. Gọi P là số lượng số đã trừ, R là độ dài còn lại: `n = P + R//d`. Cách này tránh viết tay sai các mốc; không chuyển chuỗi tới một triệu chữ số sang int. |
| 22 | [Bộ ba Pytago](https://laptrinhonline.club/problem/563296qd) | `isqrt`, `abs`, thử số ít trường hợp | Lần lượt chọn số x để sửa, giữ u,v. Bình phương cạnh mới có thể là `u*u+v*v` hoặc `abs(u*u-v*v)`. Nhận t nếu `r=isqrt(t)` thỏa `r>0` và `r*r==t`; chi phí `abs(r-x)`. Lấy min cho cả ba vị trí, không có thì -1. Bao gồm đáp án 0 nếu bộ ban đầu đã đúng. |
| 23 | [0.Cánh cửa thần kì](https://laptrinhonline.club/problem/themisutc) | List tên, `while`, `//` | Mỗi khối có 5 tên, mỗi tên lặp b lần với b=1,2,4,... Đặt b=1; khi x>5*b, trừ x đi 5*b rồi nhân đôi b. Tên cần tìm có chỉ số `(x-1)//b`. Đặt lại x/b cho mỗi truy vấn, không mô phỏng deque dài. O(log x). |
| 24 | [Lại là Lật mặt các đồng xu](https://laptrinhonline.club/problem/tichpxlllatdongxu) | `math.isqrt`, đọc nhiều test | Đồng xu i bị lật bằng số ước của i; chỉ chính phương có số ước lẻ. Ban đầu ngửa nên chính phương thành sấp, số ngửa là `n-isqrt(n)`. Không tạo n đồng xu hoặc dùng sqrt float với n tới 10¹⁸. |

<a id="nhom-iv"></a>
## IV. Phương trình và hình học

### Python cần ôn

- `float`, `math.sqrt`, `abs`, tính biểu thức với ngoặc rõ ràng.
- Hàm `def` và `return` để dùng lại cách giải phương trình/định thức.
- List, tuple tọa độ, vòng lặp lồng nhau và `itertools.combinations` nếu muốn liệt kê tổ hợp.
- F-string `.2f`, `.3f`; giữ đủ độ chính xác khi tính, chỉ định dạng lúc in.

### Chú ý chung

- Xử lý hệ số đầu bằng 0 trước khi chia; phân biệt vô nghiệm, hữu hạn nghiệm và vô số nghiệm.
- Với số thực, chọn cách so sánh gần 0 phù hợp độ lớn dữ liệu; đừng dùng một ngưỡng tùy ý cho mọi thang số hoặc chia khi chưa kiểm tra suy biến.
- Tam giác phải có các cạnh dương; hai cạnh nhỏ cộng lại bằng cạnh lớn là tam giác suy biến.
- Không làm tròn ở từng bước trung gian.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 25 | [Phương trình bậc hai](https://laptrinhonline.club/problem/tichpxptb2) | `if/elif`, `sqrt`, f-string | Giải `a*x*x+b*x+c=0`: nếu a=0 thì giải tuyến tính, kể cả b=0; nếu a≠0 thì xét delta=b²−4ac. Delta âm: vô nghiệm; bằng 0: một nghiệm; dương: hai nghiệm. In đúng mẫu của đề và xử lý nghiệm trùng một lần. |
| 26 | [Đếm số nghiệm phương trình trùng phương](https://laptrinhonline.club/problem/tichpxpttp) | Hàm giải bậc hai, kiểm tra dấu | Đặt t=x²≥0, giải `a*t*t+b*t+c=0`, lấy các nghiệm t phân biệt. Mỗi t>0 đóng góp 2 nghiệm x; t=0 đóng góp 1; t<0 không đóng góp. Các hệ số đều 0 thì vô số nghiệm, in -1. Xử lý cả a=0; không đếm đôi nghiệm kép của t. |
| 27 | [Giải và biện luận phương trình trùng phương](https://laptrinhonline.club/problem/tichpxpttp1) | `sqrt`, list nghiệm, định dạng | Cùng phép đặt t=x²; từ t>0 sinh ±sqrt(t), t=0 chỉ sinh 0. In mỗi nghiệm một dòng với 3 chữ số; không có nghiệm in `vo nghiem`, vô số nghiệm in `vo so nghiem`. Không cần sắp nếu đề không yêu cầu nhưng phải đủ nghiệm và không trùng. |
| 28 | [Ghép Hình](https://laptrinhonline.club/problem/tichpxghephinh) | Tuple, hoán đổi cạnh, `if` | Thử hai hướng đặt của mỗi hình chữ nhật. Với hai hình có cùng chiều cao h, ghép ngang thành hình vuông khi tổng hai chiều rộng bằng h. Chỉ có 4 tổ hợp hướng nên duyệt trực tiếp; in YES/NO. |
| 29 | [Thể tích khối cầu](https://laptrinhonline.club/problem/i1101) | `float`, `**`, f-string | Tính `V = (4/3)*3.14159*R**3`, in `VOLUME = ...` với 3 chữ số. Dùng đúng pi=3.14159 do đề quy định, không tự thay bằng hằng pi chính xác hơn; không dùng `4//3`. |
| 30 | [Chu vi và diện tích đa giác lồi](https://laptrinhonline.club/problem/tichpxdagiacloi) | Tuple, `sqrt` hoặc `hypot`, modulo chỉ số | Với mỗi i, nối điểm i tới `(i+1)%n`. Chu vi cộng độ dài cạnh; diện tích bằng `abs(sum(x_i*y_next-x_next*y_i))/2`. Cạnh cuối về đầu phải cùng chiều với các cạnh khác. In chu vi và diện tích mỗi giá trị 3 chữ số. O(n). |
| 31 | [Hai tam giác](https://laptrinhonline.club/problem/tichpx2tg) | 3 vòng lặp hoặc `combinations`, copy list | Chọn 3 trong 6 vị trí làm tam giác thứ nhất; 3 vị trí còn lại làm tam giác thứ hai. Với mỗi bộ, sort ba cạnh và kiểm tra tổng hai cạnh nhỏ lớn hơn cạnh lớn. Có một cách hợp lệ là yes, không có là no. Chọn theo chỉ số để xử lý cạnh trùng; không lấy hiệu set vì sẽ mất số lần xuất hiện. |
| 32 | [Hệ ba phương trình tuyến tính](https://laptrinhonline.club/problem/tichpxhe3pttt) | Hàm định thức, ma trận 3×3, số thực | Dùng Cramer: D là định thức hệ số; Dx,Dy,Dz lần lượt thay từng cột bằng vế phải. Nếu D khác 0, nghiệm là Dx/D,Dy/D,Dz/D. Nếu suy biến in `HE PHUONG TRINH SUY BIEN`. Viết một hàm định thức dùng lại, chú ý sai số số thực; in `x = ...`, `y = ...`, `z = ...` với 3 chữ số. |

<a id="nhom-v"></a>
## V. Dictionary: tra cứu, tần suất và tổng hợp

### Python cần ôn

- Khởi tạo `{}`, đọc/gán `d[key]`, kiểm tra `key in d`, `get`, `items`, `keys`, `values`.
- Mẫu đếm: `freq[x] = freq.get(x, 0) + 1`; `collections.Counter` là lựa chọn gọn hơn.
- `sorted(d)` sắp khóa; `sorted(d.items())` sắp các cặp; `zip` ghép tiêu đề với dữ liệu.
- List giữ đầy đủ các đáp án truy vấn theo lượt; dict dùng để tra cứu hoặc gom theo khóa.

### Chú ý chung

- Dict gộp khóa trùng. Nếu có hai truy vấn giống nhau, vẫn cần in hai đáp án.
- Khi ghép hai bảng theo cùng giá trị, duyệt một bảng rồi tra `.get()` ở bảng kia; tránh hai vòng dò mọi cặp khóa.
- Số viết dạng chuỗi có thể cần chuẩn hóa nếu `01` và `1` phải coi là cùng số. Riêng mã cần giữ số 0 đầu thì giữ chuỗi.
- Không mặc định `dict.values()` có thứ tự tăng dần; sắp theo yêu cầu đầu ra.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 33 | [Truy vấn tần suất chuỗi](https://laptrinhonline.club/problem/sparsearr) | Dict tần suất, `get`, list đáp án | Đếm mỗi chuỗi của S một lần. Mỗi truy vấn word trả `freq.get(word,0)`, in theo đúng thứ tự truy vấn, kể cả truy vấn trùng. Không đếm lại S cho từng truy vấn. |
| 34 | [0.Mã vùng điện thoại.](https://laptrinhonline.club/problem/i0501) | Dict cố định, `get` | Tạo bảng 61→Brasilia, 71→Salvador, 11→Sao Paulo, 21→Rio de Janeiro, 32→Juiz de Fora, 19→Campinas, 27→Vitoria, 31→Belo Horizonte. In thành phố tương ứng, không có thì `DDD nao cadastrado`. Giữ đúng dấu cách/chữ hoa trong tên. |
| 35 | [Thống kê tần suất xuất hiện](https://laptrinhonline.club/problem/tichpxtansuat) | Dict hoặc Counter, `sorted` | Đếm mỗi số, rồi duyệt `for x in sorted(freq)` để in x và số lần. Khóa là int nên sắp theo giá trị số, kể cả số âm. O(n+u log u), u là số giá trị khác nhau. |
| 36 | [Đếm giầy](https://laptrinhonline.club/problem/tichpxdemdep) | Slicing chuỗi, hai dict | Tách `side=shoe[0]`, `size=shoe[1:]`; đếm trái/phải theo size. Tổng số đôi bằng tổng `min(left[size],right.get(size,0))` trên các size bên trái. Không cần tìm và xóa từng chiếc trong list. |
| 37 | [Xây dựng lan can đường sắt Cát Linh - Hà Đông](https://laptrinhonline.club/problem/tichpxlancan) | List đếm hoặc Counter, đọc nhanh | Đếm số thanh mỗi độ dài ở hai bên; số cặp bằng tổng min hai tần suất. Với miền 1..1000 dùng hai list dài 1001 và duyệt miền giá trị. Dữ liệu lớn nên tránh giữ đồng thời list đầu vào và bảng đếm nếu không cần; giữ đúng số nguyên khi đọc. |
| 38 | [Tính điểm thi lập trình](https://laptrinhonline.club/problem/tichpxtinhdiem) | `dict(zip(...))`, dict hệ số, `int`, sort | Đọc tiêu đề để biết vị trí TEN,A,B,C,D,E. Ghép mỗi dòng với tiêu đề; tính A+2B+3C+4D+5E, lưu tên/điểm, sắp tên tăng. Không cố định vị trí cột; tên trong bài không chứa khoảng trắng. |

<a id="nhom-vi"></a>
## VI. Sắp xếp và xử lý bản ghi

### Python cần ôn

- List các tuple, unpacking, `zip`, `enumerate`, `sort`, `sorted`.
- Khóa nhiều tiêu chí: `key=lambda x: (-x[1], x[0])` nghĩa là tiêu chí thứ hai giảm, tiêu chí đầu tăng.
- Tách tên có khoảng trắng bằng `*name, age, score = line.split()` rồi `" ".join(name)`.
- Ngày sinh: `datetime.strptime(text, "%d/%m/%Y")` hoặc tuple `(year,month,day)`.
- Sort của Python ổn định: bằng khóa thì giữ thứ tự đầu vào.

### Chú ý chung

- Chuyển tuổi/điểm sang số trước khi so sánh. Chuỗi `"100"` có thể đứng trước `"19"`.
- Lưu chỉ số gốc trước khi sắp. Xóa khỏi list làm dịch chỉ số, còn `index()` trả lần xuất hiện đầu tiên.
- Chỉ thêm khóa phụ khi đề yêu cầu; thêm tên vào key có thể phá yêu cầu giữ thứ tự ban đầu khi bằng ngày sinh.
- `zip` dừng ở dãy ngắn nhất; kiểm tra dữ liệu đủ số phần tử khi ghép nhiều dãy.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 39 | [Sắp xếp có điều kiện](https://laptrinhonline.club/problem/tichpxsapxep3) | `sort`, lambda, tuple key, `%` | Sắp bằng `key=lambda x: (x%3,x)`: nhóm dư 0 trước, rồi dư 1, dư 2; trong mỗi nhóm tăng dần. Không chỉ sort theo số dư vì như vậy chưa sắp giá trị trong nhóm. |
| 40 | [Trao giải chung kết marathon](https://laptrinhonline.club/problem/tichpxckmarathon) | Unpacking từ cuối, lọc list, sort | Tách `*name,score,faculty`. Nhóm DDT sắp điểm giảm lấy 3 người; nhóm ngoài DDT lấy người điểm cao nhất làm giải giao lưu. Điểm đôi một khác nhau. In đúng các nhãn giải; tên có thể nhiều từ. |
| 41 | [Xếp hạng](https://laptrinhonline.club/problem/mrt48) | Dict tần suất, set hoặc khóa dict, sort | Đếm tần suất điểm, lấy ba mức điểm phân biệt lớn nhất rồi in số người ở từng mức theo nhãn `1st`, `2nd`, `3rd`. Không lấy ba phần tử lớn nhất của list gốc vì có thể cùng một mức điểm. Chú ý trường hợp không có đủ ba mức khi triển khai. |
| 42 | [Sắp xếp danh sách sinh viên](https://laptrinhonline.club/problem/tichpxsxdssv) | Đọc EOF, unpacking, datetime, stable sort | Mỗi dòng: `*name,birth,gender`. Đọc tới EOF, lưu bản ghi, sort chỉ theo ngày sinh tăng. Chuyển ngày thành datetime hoặc `(year,month,day)` để so đúng; người cùng ngày sinh giữ thứ tự gốc. |
| 43 | [Quản lý danh sách sinh viên](https://laptrinhonline.club/problem/tichpxdssinhvien) | Unpacking, dict, `int`, `float`, sort | Tách hai trường cuối là tuổi/điểm; tuổi chuyển int và đếm tần suất, điểm chuyển float. In thống kê tuổi tăng, rồi danh sách theo điểm giảm. Điểm in 2 chữ số; thống kê tuổi có mẫu `tuoi : count`. |
| 44 | [Vị trí sau khi sắp xếp](https://laptrinhonline.club/problem/tichpxvitrisausx) | `enumerate`, tuple, sort | Lưu `(value,index+1)` rồi sắp theo value tăng và in chỉ số gốc. Dữ liệu bài có giá trị phân biệt; lưu chỉ số vẫn tránh việc tìm/xóa liên tục. O(n log n), không làm biến đổi chỉ số của dãy gốc. |

<a id="nhom-vii"></a>
## VII. Đệ quy và quay lui

### Python cần ôn

- `def`, lời gọi hàm, `return`, biến cục bộ và biến ngoài hàm.
- List đường đi: `append` khi chọn, `pop` khi quay về.
- Set đã dùng: `add`, `remove`, kiểm tra `in`.
- Chuỗi có thể truyền nhánh bằng `s + "0"` mà không sửa chuỗi ở nhánh cha.

### Chú ý chung

- Điều kiện dừng phải `return` sau khi ghi/in đáp án hoàn chỉnh.
- Mỗi nhánh: chọn → đánh dấu → gọi đệ quy → bỏ chọn → bỏ đánh dấu.
- `count += 1` trong hàm cần `global count` nếu sửa biến ngoài, hoặc thiết kế hàm trả số đếm. Sửa nội dung list bằng `append/pop` không cần khai báo global.
- Đếm đáp án ở lá hoàn chỉnh, không đếm mỗi lần thêm một phần tử.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 45 | [Sinh các dãy nhị phân](https://laptrinhonline.club/problem/tichpxdaynp) | Đệ quy, chuỗi hoặc list | Tại mỗi vị trí thử 0 rồi 1; đủ n chữ số thì in và return. Dùng list thì pop sau mỗi lần gọi con. Số đáp án 2^n nên thời gian ít nhất tỷ lệ tổng độ dài đầu ra. |
| 46 | [0.Liệt kê hoán vị](https://laptrinhonline.club/problem/mah1) | Đệ quy, list path, set used | Mỗi bước thử i từ 1..n; bỏ qua số đã dùng; chọn, đệ quy rồi hoàn tác. Đủ n phần tử thì in theo định dạng đề. Duyệt ứng viên tăng để sinh thứ tự tăng; có n! đáp án. |
| 47 | [Hoán vị 4](https://laptrinhonline.club/problem/tichpxhoanvi4) | Quay lui, `%`, biến đếm | Sinh hoán vị như bài trước; khi path chưa rỗng, bỏ ứng viên nếu `(path[-1]+i)%4==0`. Đủ n phần tử thì in và tăng số đáp án; cuối cùng in tổng số. Đặt điều kiện cắt trước append để không đi vào nhánh sai. |

<a id="nhom-viii"></a>
## VIII. Stack và mô phỏng hàng vòng tròn

### Python cần ôn

- List làm stack: `append`, `pop`, `stack[-1]`, kiểm tra `while stack`.
- Lưu chỉ số trong stack để lấy cả giá trị và khoảng cách.
- Xóa theo chỉ số bằng `pop(index)`, modulo để quay vòng.
- Dict khối lượng nguyên tử và xử lý từng ký tự của chuỗi.

### Chú ý chung

- `pop()` bỏ cuối stack, không tự tìm phần tử nhỏ nhất như heap.
- Tránh `stack[-2] += stack.pop()` vì pop thay đổi độ dài ngay trong phép gán; tách giá trị ra biến rồi cập nhật.
- Stack đơn điệu chỉ giữ các ứng viên còn hữu ích. Điều kiện bằng nhau phải theo yêu cầu cao hơn hay cao hơn hoặc bằng.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 48 | [Khối lượng hóa chất](https://laptrinhonline.club/problem/tichpxweighthoachat) | Dict, stack số, duyệt ký tự | C,H,O đưa khối lượng 12,1,16 vào stack; `(` đưa dấu mốc; hệ số 2..9 nhân phần tử cuối. Gặp `)` thì pop và cộng tới dấu mốc, bỏ mốc, push tổng nhóm. Cuối cùng sum các giá trị. Cần hỗ trợ ngoặc lồng nhau; không cộng mất ranh giới nhóm trước khi gặp hệ số. |
| 49 | [Bịt mắt bắt dê](https://laptrinhonline.club/problem/tichpxbitmatbatde) | List, chỉ số, modulo, `pop` | Tạo người 1..n, pos=0. Khi còn hơn 1 người: `pos=(pos+k-1)%len(people)`, rồi `pop(pos)`. Người kế tiếp dịch vào vị trí vừa xóa và được đếm là 1. Chỉ số phải quay vòng theo số người còn lại. Mô phỏng O(n²) phù hợp n≤1000. |
| 50 | [Chào đón tân sinh viên K59](https://laptrinhonline.club/problem/tichpxchaodonk59) | Hai lượt stack chỉ số, list left/right | Quét trái sang phải: pop khi chiều cao đỉnh ≤ người mới; đỉnh còn lại là người cao hơn gần nhất bên trái, ghi trước khi append i. Làm tương tự từ phải sang trái với stack mới. So hai khoảng cách, hòa chọn trái; không có thì -1. In chỉ số 0-based. O(n). |

<a id="nhom-ix"></a>
## IX. Đoạn liên tục: set, tổng tích lũy và cửa sổ

### Python cần ôn

- Set kiểm tra trùng; dict lưu tần suất hoặc vị trí xuất hiện đầu.
- Tổng tiền tố: cập nhật một tổng thay vì cộng lại đoạn cũ.
- `collections.deque`, `append`, `pop`, `popleft` và chỉ số cửa sổ.

### Chú ý chung

- Set không lưu số lần xuất hiện; không xóa bừa một giá trị khỏi cửa sổ khi nó còn bản sao.
- Slicing rồi max/sum tạo nhiều công việc lặp; kiểm tra giới hạn trước khi chọn cách đó.
- Deque đơn điệu lưu ứng viên và chỉ số, không nhất thiết chứa toàn bộ cửa sổ.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 51 | [Dãy con liên tục khác biệt](https://laptrinhonline.club/problem/tichpxtapkhacbiet) | Set; tùy chọn dict vị trí cuối | Cách đã học: với mỗi đầu trái, tạo set mới, kéo phải tới khi trùng, lưu độ dài lớn nhất. O(n²) phù hợp giới hạn n≤1000 của bài. Có thể tối ưu O(n) bằng cửa sổ và vị trí xuất hiện cuối; không cần đổi chỉ để giải lại bản giới hạn nhỏ. |
| 52 | [Cổ vũ](https://laptrinhonline.club/problem/tichpxcv) | Tổng tiền tố, dict | Quy đổi X thành +1, D thành -1. Nếu tổng tiền tố bằng nhau tại hai vị trí thì đoạn giữa có số X,D bằng nhau. Khởi tạo `{0:0}`; với vị trí i, nếu tổng đã gặp thì cập nhật `i-first[total]`, chưa gặp mới lưu i. Giữ vị trí đầu tiên, không chỉ xét total=0. O(n). |
| 53 | [Trinh thám](https://laptrinhonline.club/problem/tichpxtrinhtham) | Deque chỉ số, hai vòng while | Với i: bỏ đầu có chỉ số ≤i−k; bỏ cuối có chiều cao ≤heights[i]; append i. Khi i≥k−1, max cửa sổ là `heights[q[0]]`. Có n−k+1 đáp án. Mỗi chỉ số vào/ra tối đa một lần nên O(n). Không dùng lại `max(heights[start:end])` cho dữ liệu lớn. |

<a id="nhom-x"></a>
## X. BFS/DFS, trạng thái và nhóm liên thông

### Python cần ôn

- `deque` làm queue FIFO: thêm cuối bằng `append`, lấy đầu bằng `popleft`.
- List khoảng cách `dist = [-1] * size`; ma trận khoảng cách; set các trạng thái tuple.
- Danh sách kề: `adj = [[] for _ in range(n+1)]`, cạnh vô hướng lưu hai chiều.
- Vòng lặp duyệt hàng xóm; tuple tọa độ; `%`, `isqrt` để sinh trạng thái số.
- List `parent` và `digit` để ghi đường đi; `join` và đảo danh sách để dựng đáp án.

### Chú ý chung

- Đánh dấu ngay khi phát hiện, trước khi enqueue. Set tự loại trùng trong set nhưng không tự loại trùng trong queue.
- Đưa trạng thái đầu vào queue trước `while q`, đánh dấu trạng thái đầu luôn.
- BFS cho số bước ít nhất khi mọi cạnh/bước có cùng chi phí. DFS dùng được để tìm các đỉnh tới được/nhóm, nhưng không tự cho khoảng cách ngắn nhất.
- Duyệt nhiều vùng: visited giữ xuyên suốt; queue hết mới lưu kết quả của một vùng.
- Kiểm tra đầu bằng đích, không tới đích, đỉnh cô lập, ô biên, 0-based/1-based và số hướng được phép.
- Đếm các mức khoảng cách bằng một lượt duyệt hoặc dict tần suất; gọi `dist.count(level)` cho mọi mức có thể thành O(n²).

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 54 | [Nhập môn BFS](https://laptrinhonline.club/problem/quanma) | Deque, ma trận dist, tuple | Trạng thái là ô quân mã; sinh 8 bước `(±2,±1)` và `(±1,±2)`. Trong biên và dist=-1 thì gán dist mới bằng dist cũ+1 rồi enqueue. Đầu bằng đích cho 0, không tới cho -1. Không đi chéo 1 ô như vua. |
| 55 | [Tìm đường đi ngắn nhất trong mê cung](https://laptrinhonline.club/problem/tichpxmecung) | Ma trận bản đồ và ma trận dist riêng | BFS 4 hướng từ nguồn, chỉ đi vào ô 0 chưa thăm; ô 1 là tường. Tọa độ input 1-based thì trừ 1. Khởi tạo nguồn theo đề, không tự loại nguồn chỉ vì giá trị ô đó là 1; khoảng cách để riêng khỏi bản đồ. Đáp án là dist tại đích, -1 nếu không tới. |
| 56 | [Thang Máy](https://laptrinhonline.club/problem/tichpxthangmay) | Deque số nguyên, list dist | Trạng thái là tầng u; thử u+k và u−m trong 1..n. BFS từ s, ghi số lần bấm ít nhất; in dist[f]. Gán dist[s]=0 nên s=f tự cho 0. Chưa thăm bằng -1 tránh quay vòng. |
| 57 | [Phân vùng ảnh](https://laptrinhonline.club/problem/tichpxphanvung) | Ma trận visited, deque, list diện tích | Quét từng ô; gặp ô 0 chưa thăm thì BFS theo 8 hướng, đánh dấu và đếm diện tích vùng. Queue hết mới lưu area; tiếp tục quét để tìm vùng khác. In số vùng và diện tích tăng dần. Ô trắng là 0; chéo cũng nối vùng. O(n*m). |
| 58 | [Robot](https://laptrinhonline.club/problem/tichpxrobot) | Set tuple, deque | Từ (x,y), nếu x chẵn sinh `(y,x//2)`; nếu y lẻ sinh `((y+1)//2,x)`. Hai if độc lập; thêm trạng thái chưa thăm, cuối cùng len(visited), kể cả vị trí đầu. Tọa độ 0 hợp lệ; dùng //; x lẻ/y chẵn thì không đi tiếp nhưng vị trí vẫn được đếm. |
| 59 | [Những con đường về không](https://laptrinhonline.club/problem/tichpxlietkezero) | `isqrt`, set số, deque, sorted | Với x>0, duyệt a từ 1 đến isqrt(x); nếu chia hết thì b=x//a và sinh `(a-1)*(b+1)`. Đánh dấu trước enqueue, không cần mở rộng 0. Cuối cùng in các giá trị khác nhau tăng dần, gồm cả n ban đầu. Điều kiện a≤b đã được bảo đảm khi duyệt đến căn. |
| 60 | [Liên lạc](https://laptrinhonline.club/problem/kkpy10) | Danh sách kề, set/list visited, tuple kết quả | Duyệt mỗi người chưa thăm để mở BFS một nhóm. Trong nhóm giữ chỉ số người có độ tin cậy lớn nhất; hết queue mới lưu đại diện. In số nhóm và chỉ số đại diện tăng dần. Người cô lập cũng là một nhóm; cạnh liên lạc hai chiều. |
| 61 | [Nhóm bạn](https://laptrinhonline.club/problem/tichpxnhomban) | Danh sách kề, deque, visited, bộ đếm | BFS/DFS từng nhóm chưa thăm; tăng số nhóm và đếm số người mỗi nhóm để cập nhật lớn nhất. Không bắt buộc giữ list toàn bộ thành viên nếu chỉ cần kích thước. Có thể dùng lại cách đã AC; dữ liệu nhiều dòng cần đọc nhanh, tính cả người không có cạnh. O(n+m). |
| 62 | [Phân loại các F để cách ly Covid-19](https://laptrinhonline.club/problem/tichpxcovid19) | BFS nhiều nguồn, dist, dict đếm | Đưa toàn bộ F0 vào queue và gán dist=0 trước while. BFS ghi dist[v]=dist[u]+1 lần đầu gặp. Đếm những người có dist≥0, in `F0: ...`, `F1: ...` theo mức tăng. Người không tới được không thống kê. Không chạy BFS độc lập rồi cộng kết quả từng F0. |
| 63 | [Chữ số 6 và 8](https://laptrinhonline.club/problem/tichpx68) | Deque phần dư, list parent/digit, dựng chuỗi | Khởi tạo phần dư 6%n rồi 8%n; từ r thử d=6 rồi 8 với `nr=(10*r+d)%n`. Mỗi phần dư giữ lần gặp đầu, lưu cha r và chữ số d. Gặp dư 0 thì lần cha và đảo chữ số; hết queue không gặp thì in 0. Dùng ký hiệu chưa thăm khác gốc, chẳng hạn parent=-2 chưa thăm, -1 là gốc. Queue không cần chứa cả số rất dài. |

### Khung BFS cơ bản

```python
dist = [-1] * (n + 1)
dist[start] = 0
q = deque([start])

while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
```

Với nhiều nguồn, khởi tạo mọi nguồn có dist=0 và đưa hết vào queue. Với nhiều nhóm, khởi động lại BFS từ mỗi đỉnh chưa thăm nhưng giữ chung visited.

<a id="nhom-xi"></a>
## XI. Heap và tham lam

### Python cần ôn

- `heapq.heapify`, `heappush`, `heappop`, `heap[0]`.
- Heap khởi đầu rỗng không cần heapify. Heap chứa sẵn nhiều giá trị thì heapify tại chỗ trước khi dùng.
- Min-heap cho phần tử nhỏ nhất ở đầu; muốn lấy lớn nhất bằng heapq truyền thống thì lưu số đối.
- Sort các bản ghi theo hạn chót; dict/Counter đếm tần suất.

### Chú ý chung

- `heapify` trả None; `heappush(heap,x)` cần cả heap lẫn giá trị.
- Heap không phải list đã sort toàn bộ. `heappush` không đơn giản là append mà còn sửa cấu trúc heap.
- Phân biệt đại lượng cần cộng: chi phí từng lần nối khác với tổng độ dài cuối cùng.
- Thuật toán tham lam cần quy tắc chọn cụ thể của từng bài; dùng heap chưa tự làm cho một quy tắc bất kỳ trở nên đúng.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 64 | [Nối thanh kim loại](https://laptrinhonline.club/problem/tichpxnoidam) | Min-heap, biến tổng | Heapify độ dài. Khi còn hơn một thanh, pop hai thanh nhỏ nhất a,b; cộng a+b vào chi phí rồi push a+b lại. Chỉ một thanh thì chi phí 0. O(n log n). |
| 65 | [Thuật toán mã hóa Huffman](https://laptrinhonline.club/problem/tichpxhuffman) | Dict tần suất, heap | Đếm ký tự, heapify các tần suất. Ghép hai nhỏ nhất và cộng chi phí như Nối thanh; tổng chi phí là tổng bit mã hóa khi có ít nhất hai loại ký tự. Không tính newline thành ký tự. Đề chưa nêu rõ quy ước mã cho chuỗi chỉ một loại ký tự; cần xác minh trường hợp đó khi kiểm tra, không tự coi ảnh AC chứng minh một quy ước cụ thể. |
| 66 | [Phần tử trung vị](https://laptrinhonline.club/problem/tichpxmedian) | Hai heap, số đối, cân bằng kích thước | low giữ nửa nhỏ bằng max-heap số đối, high giữ nửa lớn bằng min-heap. Thêm số vào nửa thích hợp rồi chuyển đỉnh để len(low)=len(high) hoặc hơn 1. Trung vị mỗi tiền tố là `-low[0]`; số phần tử chẵn lấy trung vị thấp, không lấy trung bình. O(n log n). |
| 67 | [Giao hàng](https://laptrinhonline.club/problem/tichpxshipper) | Sort deadline, min-heap thưởng | Sắp việc theo hạn t tăng. Với thưởng v, push v; nếu số việc chọn len(heap)>t thì pop thưởng nhỏ nhất. Cuối cùng sum(heap). Mỗi việc mất 1 đơn vị thời gian; heap là tập việc dự định làm kịp hạn, có thể thay quyết định trước đó. Phải sort trước khi so len với hạn. O(n log n). |

### Hai mẫu heap hay dùng

```python
# Nối thanh / Huffman: cộng chi phí mỗi lần ghép.
heapq.heapify(heap)
total = 0
while len(heap) > 1:
    merged = heapq.heappop(heap) + heapq.heappop(heap)
    total += merged
    heapq.heappush(heap, merged)

# Giao hàng: giữ tập thưởng tốt nhất theo hạn chót.
chosen = []
for deadline, reward in sorted(orders):
    heapq.heappush(chosen, reward)
    if len(chosen) > deadline:
        heapq.heappop(chosen)
```

<a id="nhom-xii"></a>
## XII. Quy hoạch động

### Python cần ôn

- Set các trạng thái đạt được; tạo tập mới sau mỗi lớp.
- Hai vòng lặp: trạng thái cũ × lựa chọn ở nhóm mới.
- Phép modulo để nhiều tổng khác nhau quy về cùng trạng thái.
- `max(possible)` lấy giá trị tốt nhất sau khi đã xử lý đủ mọi nhóm.

### Chú ý chung

- Xác định trạng thái đang mô tả điều gì và đã xử lý bao nhiêu nhóm.
- Không cập nhật ngay tập đang duyệt: có thể dùng cùng nhóm nhiều lần hoặc lỗi thay đổi kích thước set.
- Một phần dư nhỏ ở bước giữa vẫn có thể dẫn đến đáp án lớn nhất ở cuối; cần giữ mọi phần dư có thể đạt.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 68 | [Sức mạnh tập thể](https://laptrinhonline.club/problem/tichpxsucmanh) | Set, modulo, DP theo nhóm | Bắt đầu possible={0}. Với mỗi nhóm tạo new=set(); với mọi r cũ và x trong nhóm, thêm `(r+x*x)%M`. Hết nhóm mới gán possible=new. Cuối cùng max(possible). Bỏ số k đầu mỗi dòng vì đó là số lượng người, không phải sức mạnh. Có tối đa M trạng thái mỗi lớp, thời gian O(N*M*K), bộ nhớ O(M). |

```python
possible = {0}
for group in groups:
    new_possible = set()
    for r in possible:
        for x in group:
            new_possible.add((r + x * x) % M)
    possible = new_possible
answer = max(possible)
```

<a id="nhom-xiii"></a>
## XIII. Cây khung nhỏ nhất và DSU

### Python cần ôn

- Cạnh dạng tuple `(weight,u,v)` và sắp xếp tăng theo trọng số.
- List `parent`, `size` hoặc `rank` để quản lý các nhóm đỉnh.
- Hàm `find(x)` tìm đại diện, `union(u,v)` gộp nhóm; nén đường đi và gộp theo kích thước/hạng.
- Có thể viết find bằng vòng lặp để tránh chuỗi lời gọi đệ quy dài.

### Chú ý chung

- Cây khung nhỏ nhất tối thiểu hóa tổng trọng số để nối mọi đỉnh. Bài đường đi ngắn nhất từ nguồn có mục tiêu khác.
- Đỉnh cùng nhóm thì thêm cạnh giữa chúng sẽ tạo chu trình; DSU kiểm tra điều đó.
- List parent của DSU biểu diễn nhóm đang gộp; parent trong BFS dựng đường đi có mục đích khác, dù cùng tên biến.

### Cách làm từng bài

| STT | Bài | Python sử dụng | Cách làm và chú ý |
|---:|---|---|---|
| 69 | [Cây khung nhỏ nhất](https://laptrinhonline.club/problem/tichpxmst) | Kruskal, sort cạnh, DSU | Khởi tạo mỗi đỉnh một nhóm, sắp cạnh tăng. Với cạnh (w,u,v), nếu find(u) khác find(v) thì cộng w, gộp nhóm và tăng số cạnh chọn. Đủ n−1 cạnh thì dừng; đề cho đồ thị liên thông. Dùng nén đường đi cùng gộp theo kích thước/hạng. Tổng thời gian chủ yếu O(m log m) do sort. |

## Những lỗi cần rà khi ôn lại

- **Đổi cơ số:** tránh log số thực ở lũy thừa của cơ số.
- **Vòng lặp:** tính độ dài theo khối để tránh sai dấu/mốc ở nhóm 6 chữ số.
- **Bản ghi sinh viên:** tuổi cần int trước khi đếm/sắp.
- **BFS:** đầu bằng đích, không tới được, đánh dấu trước enqueue và lưu kết quả nhóm sau khi queue hết.
- **Truy vấn tần suất:** cùng truy vấn nhiều lần vẫn phải xuất đủ nhiều dòng.
- **Trinh thám/K59:** deque/stack chứa chỉ số; lấy chiều cao qua `heights[index]`.
- **Giao hàng:** sort hạn chót trước; heap tự sửa thứ tự, không giống append vào list thường.
- **Quay lui:** return ở lá và hoàn tác sau lời gọi con.

Các tên bài trong tài liệu liên kết tới đề gốc để kiểm tra lại định dạng vào/ra. Các đoạn mẫu là khung thuật toán; cần thêm phần nhập và định dạng đúng bài trước khi nộp.
