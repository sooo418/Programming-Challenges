## 2020.01.13

### 3n+1.py

어떤 수열을 만들어내는 다음과 같은 알고리즘을 생각해보자. 어떤 정수 n에서 시작해 n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다. 이렇게 해서 새로 만들어진 숫자를 n으로 놓고 n=1이 될 때까지 같은 작업을 계속 반복한다. 예를 들어, n=22이면 다음과 같은 수열이 만들어진다.

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

아직 증명되진 않았지만 모든 정수 n에 대해 이 알고리즘을 적용시키면 결국에는 n=1에 이르게 되는 것으로 추측된다. 그리고 이 가설은 적어도 1,000,000까지의 정수에 대해서는 참이다.

n이라는 값이 입력되었을 때 1이 나올 때까지 만들어진 수의 개수(1 포함)를 n의 사이클 길이(cycle-length)라고 한다. 위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다. i와 j라는 두 개의 수가 주어졌을 떄 i와 j사이의 모든 수(i,j 포함)에 대해 최대 사이클 길이를 구하라.

#### >> 입력

입력은 일련의 정수쌍 i와 j로 구성되며 한 줄에 한 쌍의 수가 입력된다. 모든 정수는 1,000,000보다 작고 0보다 크다.

#### >> 출력

각 정수쌍 i와 j에 대해 i와 j를 입력된 순서대로 출력하고 i와 j 사이(i,j 포함)의 최대 사이클 길이를 출력한다. 이 세 수는 각각 하나씩의 스페이스로 구분되어야 하며 세 수가 모든 한 줄에 출력되어야 하고 입력된 각 줄마다 한 줄씩 출력해야 한다.

#### >> 입력 예											 >> 출력 예

1 10																	  1 10 20

100 200																100 200 125

201 210																201 210 89

900 1000															  900 1000 174



### 지뢰 찾기(Minesweeper)

지뢰 찾기를 해본 적이 있는 독자들이 많을 것이다. 이름은 잘 기억나지 않지만 어떤 운영체제에 이 작고 귀여운 게임이 깔려있다. 지뢰 찾기는 <b>M</b> <i>X</i> <b>N</b> 크기의 지뢰밭에서 모든 지뢰의 위치를 찾아내는 게임이다.

이 게임에서는 각 칸에 인접한 칸에 몇 개의 지뢰가 있는지를 보여준다. 각 칸에는 최대 여덟 개의 인접한 칸이 있을 수 있다. 아래에서 왼쪽에 있는 4 X 4 지뢰밭에는 지뢰 두 개가 있으며 각각은 '<b>*</b>' 문자로 표시되어 있다. 이 지뢰밭을 방금 설명한 힌트 숫자로 표기하면 오른쪽에 있는 것과 같은 필드가 만들어진다.

<img width="330" alt="스크린샷 2020-01-15 23 16 44" src="https://user-images.githubusercontent.com/50854729/72442045-1eb34d00-37ef-11ea-844f-958a1a6cf8d5.png"  >

#### >> 입력

입력은 임의 개수의 지뢰밭으로 구성된다. 각 지뢰밭의 첫번째 줄에는 각각 행과 열의 개수를 나타내는 두 개의 정수 n과 m(0<n, m<=100)이 들어있다. 그 다음 줄부터는 n개의 줄에 걸쳐서 각 줄마다 정확하게 m 지뢰가 없는 칸은 '<b>.</b>'으로, 지뢰는 '*****'로 표시되며 이때 따옴표는 쓰지 않는다. n=m=0인 줄은 입력이 끝났음을 나타내는 것이므로 그 줄은 처리하지 않는다.

#### >> 출력

각 지뢰밭에 대해 Field #x:라고 적혀있는 메시지를 출력한다. 이때 x는 필드 번호를 나타내며 1에서 시작한다. 그 다음 줄부터는 n개의 줄에 걸쳐서 '<b>.</b>' 문자 대신 그 칸에 인접한 칸에 들어있는 지뢰의 개수를 출력한다. 각 지뢰밭에 대한 출력 사이에는 반드시 빈 줄이 하나씩 있어야 한다.

#### >>입력 예										>> 출력 예

4  4																Field #1:

<p>*...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*100</p>

<p>....&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2210</p>

<p>.*..&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1*10</p>

<p>....&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1110</p>



3  5																Field #2:

<p>**...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**100</p>

<p>.....&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33200</p>

<p>.*...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1*100</p>



0  0