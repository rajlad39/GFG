<h2><a href="#">Min Cost To Make Two Strings IdenticalPushing...</a></h2>
<h3>Difficulty: Medium</h3><hr>
<p class="isSelectedEnd"><span style="font-size: 14pt;">Given two strings <strong>s1</strong> and <strong>s2</strong>, and two integers <strong>costS1</strong> and <strong>costS2</strong>, where costS1 is the cost of deleting one character from s1 and costS2 is the cost of deleting one character from s2, find the minimum cost required to make the two strings identical.</span></p><p><span style="font-size: 14pt;">You can delete any number of characters from either string, but the order of the remaining characters must be preserved.</span></p><p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p><pre><span style="font-size: 14pt;"><strong>Input:</strong> s1 = "abcd", s2 = "acdb", costS1 = 10, costS2 = 20
<strong>Output:</strong> 30
<strong>Explanation: </strong>Delete 'b' from both strings to obtain "acd". The total cost is 10 + 20 = 30.</span></pre><pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "ef", s2 = "gh", costS1 = 10, costS2 = 20
<strong>Output: </strong>60
<strong>Explanation: </strong>The two strings have no common characters, so delete all characters from both strings. The total cost is (2 × 10) + (2 × 20) = 60.
</span></pre>