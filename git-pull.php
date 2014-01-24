<?php
$out = array();
exec('git pull',$out);
exec('bundle exec jekyll build',$out);
echo '<html><body><pre>';
print_r($out);
echo '</pre></body></html>';
?>
