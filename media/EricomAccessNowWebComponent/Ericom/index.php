<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<script language="javascript" type="text/javascript" src="niceforms.js"></script>
<script language="javascript" type="text/javascript" src="jquery.js"></script>
<link rel="stylesheet" type="text/css" media="all" href="niceforms-default.css" />
<?php if(isset($_POST['submit']))
{
    $unchecked = 0;
    $checked = 1;
    if(isset($_POST['address']))
    {
        setcookie("EAN_address", $_POST['address']);
    }
    else
    {
        setcookie("EAN_address", "");
    }
    
    if(isset($_POST['full_address']))
    {
        setcookie("EAN_full_address", $_POST['full_address']);
    }
    else
    {
        setcookie("EAN_full_address", "");
    }
    
    if(isset($_POST['username']))
    {
        setcookie("EAN_username", $_POST['username']);
    }
    else
    {
        setcookie("EAN_username", "");
    }
    
    if(isset($_POST['password']))
    {
        setcookie("EAN_password", $_POST['password']);
    }
    else
    {
        setcookie("EAN_password", "");
    }
    
    if(isset($_POST['domain']))
    {
        setcookie("EAN_domain", $_POST['domain']);
    }
    else
    {
        setcookie("EAN_domain", "");
    }
    
    if(isset($_POST['encryption']))
    {
        setcookie("EAN_encryption", $checked);
    }
    else
    {
        setcookie("EAN_encryption", $unchecked);
    }
    
    if(isset($_POST['blaze_acceleration']))
    {
        setcookie("EAN_blaze_acceleration", $checked);
    }
    else
    {
        setcookie("EAN_blaze_acceleration", $unchecked);
    }
    
    if(isset($_POST['blaze_image_quality']))
    {
        setcookie("EAN_blaze_image_quality", $_POST['blaze_image_quality']);
    }
    else
    {
        setcookie("EAN_blaze_image_quality", "");
    }
    
    if(isset($_POST['resolution']))
    {
        setcookie("EAN_resolution", $_POST['resolution']);
    }
    else
    {
        setcookie("EAN_resolution", "");
    }
    
    if(isset($_POST['use_gateway']))
    {
        setcookie("EAN_use_gateway", $checked);
    }
    else
    {
        setcookie("EAN_use_gateway", $unchecked);
    }
    
    if(isset($_POST['gateway_address']))
    {
        setcookie("EAN_gateway_address", $_POST['gateway_address']);
    }
    else
    {
        setcookie("EAN_gateway_address", "");
    }
    
    if(isset($_POST['remoteapplicationmode']))
    {
        setcookie("EAN_remoteapplicationmode", $checked);
    }
    else
    {
        setcookie("EAN_remoteapplicationmode", $unchecked);
    }
    
    if(isset($_POST['alternate_shell']))
    {
        setcookie("EAN_alternate_shell", $_POST['alternate_shell']);
    }
    else
    {
        setcookie("EAN_alternate_shell", "");
    }
    
    if(isset($_POST['shell_working_directory']))
    {
        setcookie("EAN_shell_working_directory", $_POST['shell_working_directory']);
    }
    else
    {
        setcookie("EAN_shell_working_directory", "");
    }
    ?>
    <script>
        window.location = "../../start.html?autostart=true";
    </script>
    <?php
}
else
{
?>
<form style="margin-top:-40px;" action="index.php" method="post" class="niceform">
	<fieldset>
    	<legend>General</legend>
        <dl>
        	<dt><label for="address">Server:</label></dt>
            <dd><input type="text" name="address" id="address" size="32" maxlength="128" value="rdpdemo.ericom.com"/></dd>
        </dl>
        <dl>
        	<dt><label for="full_address"><u>R</u>DP Host:</label></dt>
            <dd><input type="text" name="full_address" id="full_address" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="username"><u>U</u>ser name:</label></dt>
            <dd><input type="text" name="username" id="username" size="32" maxlength="32" value="demo"/></dd>
        </dl>
        <dl>
        	<dt><label for="password"><u>P</u>assword:</label></dt>
            <dd><input type="password" name="password" id="password" size="32" maxlength="32" value="demo"/></dd>
        </dl>
        <dl>
        	<dt><label for="domain">Domain:</label></dt>
            <dd><input type="textbox" name="domain" id="domain" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="encryption">SSL encryption:</label></dt>
            <dd><input type="checkbox" name="encryption" id="encryption"/></dd>
        </dl>
        <dl>
        	<dt><label for="blaze_acceleration">Compression:</label></dt>
            <dd><input type="checkbox" name="blaze_acceleration" id="blaze_acceleration" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="blaze_image_quality">Acceleration:</label></dt>
            <dd>
            	<select size="1" name="blaze_image_quality" id="blaze_image_quality">
                    <option value="20">Fastest / Fair Quality</option>
		            <option value="40">Very Fast / Good Quality</option>
		            <option value="75" selected="selected">Fast / High Quality (Recommended)</option>
		            <option value="95">Good / Very High Quality</option>
                </select>
            </dd>
        </dl>
        <dl>
        	<dt><label for="resolution">Resolution:</label></dt>
            <dd>
            	<select size="1" name="resolution" id="resolution">
                    <option value="browser" selected="selected">Fit to browser window</option>
		            <option value="screen">Fit to screen</option>
	                <option value="640, 480">640 x 480</option>
		            <option value="800, 600">800 x 600</option>
		            <option value="1024, 768">1024 x 768</option>
                    <option value="1280, 720">1280 x 720</option>
                    <option value="1280, 768">1280 x 768</option>
                    <option value="1280, 1024">1280 x 1024</option>
                    <option value="1440, 900">1440 x 900</option>
                    <option value="1440, 1050">1440 x 1050</option>
                    <option value="1600, 1200">1600 x 1200</option>
                    <option value="1680, 1050">1680 x 1050</option>
                    <option value="1920, 1080">1920 x 1080</option>
                    <option value="1920, 1200">1920 x 1200</option>	
                </select>
            </dd>
        </dl>

    </fieldset>
    <fieldset>
        <legend>Advanced</legend>
        <a id="advancedToggle" href="javascript:void()" style="color:Green; position:absolute; margin-left:90px; margin-top:-25px;">open</a>
        <div id="advanced">
        <dl>
        	<dt><label for="use_gateway">Use Gateway:</label></dt>
            <dd><input type="checkbox" name="use_gateway" id="use_gateway" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="gateway_address">Gateway:</label></dt>
            <dd><input type="textbox" name="gateway_address" id="gateway_address" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="remoteapplicationmode">Start on connect:</label></dt>
            <dd><input type="checkbox" name="remoteapplicationmode" id="remoteapplicationmode" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="alternate_shell">Path name:</label></dt>
            <dd><input type="textbox" name="alternate_shell" id="alternate_shell" size="32" maxlength="32" /></dd>
        </dl>
        <dl>
        	<dt><label for="shell_working_directory">Start folder:</label></dt>
            <dd><input type="textbox" name="shell_working_directory" id="shell_working_directory" size="32" maxlength="32" /></dd>
        </dl>
        </div>
        <script>
            $('#advanced').slideToggle(1);
            $('#advancedToggle').click(function() {
                if($('#advancedToggle').html() == "open")
                {
                    $('#advanced').slideDown();
                    $('#advancedToggle').html("close");
                }
                else if($('#advancedToggle').html() == "close")
                {
                    $('#advanced').slideUp();
                    $('#advancedToggle').html("open");
                }
            });
        </script>
    </fieldset>
    <fieldset class="action">

    	<input type="submit" name="submit" id="submit" value="Submit" />

    </fieldset>
</form>
<?php
}
?>