#Import Python Packages
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


response = """ 
<table style="width: 100%">
            
                    <tbody><tr bgcolor="#fff2b9" style="border-spacing: 0px">
                            <td colspan="3" bgcolor="#fff2b9">
                                <span id="ctl00_ContentPlaceHolder1_lblServicesIn">These services serve all or part of Mississauga Halton</span>
                                <!-- 'View French Services' Link Hidden - Delete If they haven't changed their mind by Sept 2019 -->
                                <div style="float: right; display: none;">
                                    <a href="/servicesProvidedInFrench.aspx" class="noborder">
                                        <img id="ctl00_ContentPlaceHolder1_imgFrenchServices" title="French language services or programs offered to customers/clients on a consistent basis." class="FrImage" src="gfx/french-services.png" style="border-width:0px;"></a>
                                    <img src="gfx/indent.gif" alt="" style="vertical-align: middle;">
                                    <a href="listFrenchServices.aspx?id=10345">
                                        <span id="ctl00_ContentPlaceHolder1_lblListFrenchServices">View French services</span></a> &nbsp;
                                </div>
                            </td>
                        </tr>
                        
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl00_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl00_lnkService" href="displayService.aspx?id=147674">A Plus Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl00_lblAddress" class="regtext">801 Dundas St E, Mississauga, ON&nbsp;&nbsp;L4Y 4G9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl00_lblPhone" class="regtext">905-566-8633</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl00_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl00$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_lnkService" href="displayService.aspx?id=170566">Abbeywood Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_lblAddress" class="regtext">1395 Abbeywood Dr, Unit 3, Oakville, ON&nbsp;&nbsp;L6M 3B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_lblPhone" class="regtext">905-847-2221</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl01_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl01$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_lnkService" href="displayService.aspx?id=154389">Agnes Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_lblAddress" class="regtext">25 Agnes St, Unit 3, Mississauga, ON&nbsp;&nbsp;L5B 3X7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_lblPhone" class="regtext">905-272-0303</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl02_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl02$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_lnkService" href="displayService.aspx?id=151443">Albion Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_lblAddress" class="regtext">900 Albion Rd, Unit A1, Etobicoke, ON&nbsp;&nbsp;M9V 1A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_lblPhone" class="regtext">416-740-5500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl03_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl03$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_lnkService" href="displayService.aspx?id=147681">All Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_lblAddress" class="regtext">2233 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5A 2E9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_lblPhone" class="regtext">905-290-7451</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl04_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl04$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_lnkService" href="displayService.aspx?id=147744">Allwell Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_lblAddress" class="regtext">4665 Central Pkwy E, Unit 14, Mississauga, ON&nbsp;&nbsp;L4Z 2V5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_lblPhone" class="regtext">905-890-7775</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl05_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl05$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_lnkService" href="displayService.aspx?id=154816">Alpha Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_lblAddress" class="regtext">308 Guelph St, Georgetown, ON&nbsp;&nbsp;L7G 4B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_lblPhone" class="regtext">905-702-1500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl06_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl06$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_lnkService" href="displayService.aspx?id=147677">Angel Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_lblAddress" class="regtext">Erin Centre Plaza, 3955 Erin Centre Blvd, Mississauga, ON&nbsp;&nbsp;L5M 0H1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_lblPhone" class="regtext">905-820-1011</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl07_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl07$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_lnkService" href="displayService.aspx?id=147682">Apple-Hills Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_lblAddress" class="regtext">1221 Bloor St E, Mississauga, ON&nbsp;&nbsp;L4Y 2N8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_lblPhone" class="regtext">905-625-3268</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl08_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl08$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_lnkService" href="displayService.aspx?id=196655">ARC Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_lblAddress" class="regtext">2520 Eglinton Ave W, Unit 3, Mississauga, ON&nbsp;&nbsp;L5M 0Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_lblPhone" class="regtext">905-997-7999</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl09_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl09$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_lnkService" href="displayService.aspx?id=173592">Bayshore HealthCare - Mississauga - Administration Office</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_lblAddress" class="regtext">2101 Hadwen Rd, Mississauga, ON&nbsp;&nbsp;L5K 2L3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_lblPhone" class="regtext">1-877-289-3997</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl10_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl10$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_lnkService" href="displayService.aspx?id=193565">Bonafide Compounding Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_lblAddress" class="regtext">1598 Leger Way, Unit 5, Milton, ON&nbsp;&nbsp;L9E 0B9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_lblPhone" class="regtext">905-636-7880</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl11_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl11$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_lnkService" href="displayService.aspx?id=154919">Bristol Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_lblAddress" class="regtext">Winston Park Medical Centre, 2315 Bristol Circle, Suite 105, Oakville, ON&nbsp;&nbsp;L6H 6P8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_lblPhone" class="regtext">905-829-4495</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl12_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl12$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_lnkService" href="displayService.aspx?id=147684">Bristol Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_lblAddress" class="regtext">Bristol Place, 512 Bristol Rd W, Unit 10B, Mississauga, ON&nbsp;&nbsp;L5R 3Z1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_lblPhone" class="regtext">905-502-6400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl13_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl13$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_lnkService" href="displayService.aspx?id=187035">Britannia Health Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_lblAddress" class="regtext">2275 Britannia Rd W, Unit 9, Mississauga, ON&nbsp;&nbsp;L5M 2G6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_lblPhone" class="regtext">905-286-0001</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl14_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl14$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_lnkService" href="displayService.aspx?id=147685">Britannia Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_lblAddress" class="regtext">5925 Grossbeak Dr, Unit 9, Mississauga, ON&nbsp;&nbsp;L5N 6S5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_lblPhone" class="regtext">905-785-1500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl15_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl15$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_lnkService" href="displayService.aspx?id=147679">Britannia Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_lblAddress" class="regtext">5980 Churchill Meadows Blvd, Unit 11, Mississauga, ON&nbsp;&nbsp;L5M 7M5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_lblPhone" class="regtext">905-286-4830</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl16_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl16$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_lnkService" href="displayService.aspx?id=154920">Bronte Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_lblAddress" class="regtext">78 Jones St, Oakville, ON&nbsp;&nbsp;L6L 6C5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_lblPhone" class="regtext">905-847-0002</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl17_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl17$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_lnkService" href="displayService.aspx?id=154921">Bronte Creek Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_lblAddress" class="regtext">Bronte Plaza, 2290 Lake Shore Rd W, Oakville, ON&nbsp;&nbsp;L6L 1H3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_lblPhone" class="regtext">905-465-1669</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl18_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl18$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_lnkService" href="displayService.aspx?id=176137">Bronte Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_lblAddress" class="regtext">Bronte Professional Place, 330 Bronte St S, Unit 121, Milton, ON&nbsp;&nbsp;L9T 7X1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_lblPhone" class="regtext">905-875-2151</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl19_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl19$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_lnkService" href="displayService.aspx?id=147686">Burnhamthorpe Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_lblAddress" class="regtext">350 Burnhamthorpe Rd E, Unit 4, Mississauga, ON&nbsp;&nbsp;L5A 3S5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_lblPhone" class="regtext">905-270-9990</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl20_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl20$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_lnkService" href="displayService.aspx?id=147687">Calea</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_lblAddress" class="regtext">2785 Skymark Ave, Unit 2, Mississauga, ON&nbsp;&nbsp;L4W 4Y3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_lblPhone" class="regtext">905-283-3520 or 905-624-1234</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl21_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl21$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_lnkService" href="displayService.aspx?id=154876">Campbellville Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_lblAddress" class="regtext">35 Crawford Cres, PO Box 405, Campbellville, ON&nbsp;&nbsp;L0P 1B0</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_lblPhone" class="regtext">905-854-0313</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl22_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl22$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_lnkService" href="displayService.aspx?id=176223">Canadian Place Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_lblAddress" class="regtext">1055 Canadian Place, Unit 112 and 113, Mississauga, ON&nbsp;&nbsp;L4W 0C2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_lblPhone" class="regtext">905-232-3004</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl23_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl23$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_lnkService" href="displayService.aspx?id=197289">Capital Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_lblAddress" class="regtext">3075 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5A 2G9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_lblPhone" class="regtext">905-232-1099</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl24_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl24$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_lnkService" href="displayService.aspx?id=147735">Cawthra Drug Store</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_lblAddress" class="regtext">680 Silver Creek Blvd, Unit 7, Mississauga, ON&nbsp;&nbsp;L5A 3Z1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_lblPhone" class="regtext">905-277-1236</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl25_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl25$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_lnkService" href="displayService.aspx?id=147693">Central All Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_lblAddress" class="regtext">City Centre Medical Arts Building, 3420 Hurontario St, Unit 105, Mississauga, ON&nbsp;&nbsp;L5B 4A9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_lblPhone" class="regtext">905-306-0606</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl26_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl26$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_lnkService" href="displayService.aspx?id=147689">Central Parkway Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_lblAddress" class="regtext">1300 Central Pkwy W, Unit 106, Mississauga, ON&nbsp;&nbsp;L5C 4G8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_lblPhone" class="regtext">905-272-2400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl27_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl27$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_lnkService" href="displayService.aspx?id=147690">Centre City Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_lblAddress" class="regtext">5560 McAdam Rd, Mississauga, ON&nbsp;&nbsp;L4Z 1P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_lblPhone" class="regtext">905-804-0555</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl28_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl28$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_lnkService" href="displayService.aspx?id=147691">Century City Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_lblAddress" class="regtext">5025 Heatherleigh Ave, Unit 6, Mississauga, ON&nbsp;&nbsp;L5V 2Y7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_lblPhone" class="regtext">905-507-8870</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl29_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl29$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_lnkService" href="displayService.aspx?id=154390">Ceremonial Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_lblAddress" class="regtext">223 Ceremonial Dr, Unit 2, Mississauga, ON&nbsp;&nbsp;L5R 2N3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_lblPhone" class="regtext">905-712-1743</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl30_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl30$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_lnkService" href="displayService.aspx?id=147848">Chase Pharmacy (The)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_lblAddress" class="regtext">1675 The Chase, Units 1-2, Mississauga, ON&nbsp;&nbsp;L5M 5Y7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_lblPhone" class="regtext">905-828-8877</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl31_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl31$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_lnkService" href="displayService.aspx?id=147692">Churchill Meadows Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_lblAddress" class="regtext">3050 Artesian Dr, Unit 5, Mississauga, ON&nbsp;&nbsp;L5M 7P5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_lblPhone" class="regtext">905-828-7707</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl32_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl32$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_lnkService" href="displayService.aspx?id=147696">City Gate Drug Store</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_lblAddress" class="regtext">220 Burnhamthorpe Rd W, Unit 105, Mississauga, ON&nbsp;&nbsp;L5B 4N4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_lblPhone" class="regtext">905-566-4740</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl33_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl33$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_lnkService" href="displayService.aspx?id=196558">Clear View Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_lblAddress" class="regtext">1140 Winston Churchill Blvd, Unit A6, Oakville, ON&nbsp;&nbsp;L6J 0A3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_lblPhone" class="regtext">905-829-2004</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl34_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl34$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_lnkService" href="displayService.aspx?id=147698">Cliffway Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_lblAddress" class="regtext">2560 Shepard Ave, Unit 2, Mississauga, ON&nbsp;&nbsp;L5A 4E1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_lblPhone" class="regtext">905-276-8198</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl35_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl35$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_lnkService" href="displayService.aspx?id=153287">Cloverdale Clinic Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_lblAddress" class="regtext">Etobicoke Mews Plaza, 225 The East Mall, Unit 9, Toronto, ON&nbsp;&nbsp;M9B 6J1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_lblPhone" class="regtext">416-207-0333</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl36_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl36$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_lnkService" href="displayService.aspx?id=147849">Collegeway Pharmacy (The)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_lblAddress" class="regtext">2686 The Collegeway, Mississauga, ON&nbsp;&nbsp;L5L 2M9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_lblPhone" class="regtext">905-607-7333</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl37_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl37$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_lnkService" href="displayService.aspx?id=154926">Compounding Centre (The) - Oakville - Postmaster Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_lblAddress" class="regtext">2540 Postmaster Dr, Oakville, ON&nbsp;&nbsp;L6M 0N2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_lblPhone" class="regtext">905-469-9988</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl38_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl38$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_lnkService" href="displayService.aspx?id=147700">Confederation Drug Store</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_lblAddress" class="regtext">3050 Confederation Pkwy, Unit 107, Mississauga, ON&nbsp;&nbsp;L5B 3Z6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_lblPhone" class="regtext">905-306-7393</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl39_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl39$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_lnkService" href="displayService.aspx?id=147701">Cooksville Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_lblAddress" class="regtext">3035 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5A 2G9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_lblPhone" class="regtext">905-896-8788</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl40_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl40$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_lnkService" href="displayService.aspx?id=177402">Cornwall Pharmacy and Compounding Centre</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_lblAddress" class="regtext">1525 Cornwall Rd, Unit 18, Oakville, ON&nbsp;&nbsp;L6J 0B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_lblPhone" class="regtext">905-849-0909</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl41_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl41$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_lnkService" href="displayService.aspx?id=160461">Costco Pharmacy - Mississauga - Dundas St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_lblAddress" class="regtext">1570 Dundas St E, Mississauga, ON&nbsp;&nbsp;L4X 1L4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_lblPhone" class="regtext">905-566-2410</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl42_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl42$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_lnkService" href="displayService.aspx?id=147703">Costco Pharmacy - Mississauga - Laird Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_lblAddress" class="regtext">3180 Laird Rd, Mississauga, ON&nbsp;&nbsp;L5L 6A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_lblPhone" class="regtext">905-828-3368</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl43_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl43$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_lnkService" href="displayService.aspx?id=147702">Costco Pharmacy - Mississauga - Rodeo Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_lblAddress" class="regtext">5900 Rodeo Dr, Mississauga, ON&nbsp;&nbsp;L5R 3S9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_lblPhone" class="regtext">905-568-8037</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl44_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl44$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_lnkService" href="displayService.aspx?id=147704">Courtesy Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_lblAddress" class="regtext">Clarkson Rd Plaza, 1603 Clarkson Rd N, Mississauga, ON&nbsp;&nbsp;L5J 2X1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_lblPhone" class="regtext">905-823-4664</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl45_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl45$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_lnkService" href="displayService.aspx?id=147705">Creditview Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_lblAddress" class="regtext">Deer Run Plaza, 4040 Creditview Rd, Mississauga, ON&nbsp;&nbsp;L5C 3Y8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_lblPhone" class="regtext">905-275-6006</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl46_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl46$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_lnkService" href="displayService.aspx?id=193496">Cross Lake Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_lblAddress" class="regtext">760 Lakeshore Rd E, Unit 104, Mississauga, ON&nbsp;&nbsp;L5E 1C7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_lblPhone" class="regtext">905-891-9800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl47_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl47$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl48_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl48_lnkService" href="displayService.aspx?id=195693">Danton Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl48_lblAddress" class="regtext">7025 Danton Promenade, Unit 2, Mississauga, ON&nbsp;&nbsp;L5N 5E5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl48_lblPhone" class="regtext">905-785-9222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl48_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl48$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_lnkService" href="displayService.aspx?id=191189">Derry Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_lblAddress" class="regtext">Meadowvale North Shopping Centre, 6990 Financial Dr, Unit 2G, Mississauga, ON&nbsp;&nbsp;L5N 8J4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_lblPhone" class="regtext">289-785-4383</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl49_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl49$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_lnkService" href="displayService.aspx?id=154883">Derry Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_lblAddress" class="regtext">Derry Medical Centre, 6990 Derry Rd, Unit 101, Milton, ON&nbsp;&nbsp;L9T 7H3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_lblPhone" class="regtext">905-875-3784</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl50_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl50$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_lnkService" href="displayService.aspx?id=147709">Dixie Village Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_lblAddress" class="regtext">3615 Dixie Rd, Unit 10, Mississauga, ON&nbsp;&nbsp;L4Y 4H4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_lblPhone" class="regtext">905-238-6063</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl51_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl51$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_lnkService" href="displayService.aspx?id=147710">Dixie-5 Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_lblAddress" class="regtext">1185 Dundas St E, Mississauga, ON&nbsp;&nbsp;L4Y 2C6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_lblPhone" class="regtext">905-896-1313</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl52_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl52$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_lnkService" href="displayService.aspx?id=147711">Dream Crest Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_lblAddress" class="regtext">1010 Dream Crest Rd, Unit 6, Mississauga, ON&nbsp;&nbsp;L5V 3A4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_lblPhone" class="regtext">905-813-5666</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl53_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl53$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_lnkService" href="displayService.aspx?id=154944">Drug Basics Pharmacy - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_lblAddress" class="regtext">478 Dundas St W, Oakville, ON&nbsp;&nbsp;L6H 6Y3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_lblPhone" class="regtext">905-257-5400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl54_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl54$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_lnkService" href="displayService.aspx?id=176180">DrugSmart Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_lblAddress" class="regtext">Lester B Pearson International Airport, Terminal 1, Level 2, EB 2201, 6301 Silver Dart Dr, Mississauga, ON&nbsp;&nbsp;L5P 1B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_lblPhone" class="regtext">1-844-759-4325</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl55_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl55$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_lnkService" href="displayService.aspx?id=178345">Dunbloor Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_lblAddress" class="regtext">5115 Dundas St W, Toronto, ON&nbsp;&nbsp;M9A 1C1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_lblPhone" class="regtext">416-482-1980 ext 5</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl56_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl56$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_lnkService" href="displayService.aspx?id=147718">Dundas Clinical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_lblAddress" class="regtext">55 Dundas St E, Unit 1, Mississauga, ON&nbsp;&nbsp;L5A 1W1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_lblPhone" class="regtext">905-277-8822</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl57_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl57$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_lnkService" href="displayService.aspx?id=153466">Dundas Kipling Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_lblAddress" class="regtext">5359 Dundas St W, Toronto, ON&nbsp;&nbsp;M9B 1B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_lblPhone" class="regtext">416-233-2222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl58_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl58$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_lnkService" href="displayService.aspx?id=147719">Dundas Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_lblAddress" class="regtext">1133 Dundas St E, Unit 8, Mississauga, ON&nbsp;&nbsp;L4Y 2C3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_lblPhone" class="regtext">905-232-8848</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl59_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl59$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_lnkService" href="displayService.aspx?id=182999">Dundas427 Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_lblAddress" class="regtext">2200 Dundas St E, Unit 4A, Mississauga, ON&nbsp;&nbsp;L4X 2V3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_lblPhone" class="regtext">905-232-0710</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl60_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl60$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_lnkService" href="displayService.aspx?id=163930">Dunwin Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_lblAddress" class="regtext">2111 Dunwin Dr, Unit 6, Mississauga, ON&nbsp;&nbsp;L5L 3C1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_lblPhone" class="regtext">905-828-8898</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl61_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl61$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_lnkService" href="displayService.aspx?id=154922">Edward's Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_lblAddress" class="regtext">170 Rebecca St, Oakville, ON&nbsp;&nbsp;L6K 1J6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_lblPhone" class="regtext">905-338-9911</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl62_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl62$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_lnkService" href="displayService.aspx?id=147721">eMichael Pharmacy &amp; Medical Center</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_lblAddress" class="regtext">802 Southdown Rd, Unit C4, Mississauga, ON&nbsp;&nbsp;L5J 2Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_lblPhone" class="regtext">289-628-1920</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl63_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl63$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_lnkService" href="displayService.aspx?id=147724">Erindale Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_lblAddress" class="regtext">1101 McBride Ave, Mississauga, ON&nbsp;&nbsp;L5C 1M6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_lblPhone" class="regtext">905-270-1200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl64_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl64$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_lnkService" href="displayService.aspx?id=170081">Excellent Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_lblAddress" class="regtext">3885 Duke of York Blvd, Unit C106, Mississauga, ON&nbsp;&nbsp;L5B 0E4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_lblPhone" class="regtext">905-232-2111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl65_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl65$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_lnkService" href="displayService.aspx?id=187031">Extra Mile Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_lblAddress" class="regtext">Crosscurrent Centre, 2980 Crosscurrent Dr, Unit 6, Mississauga, ON&nbsp;&nbsp;L5N 7C7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_lblPhone" class="regtext">905-785-7888</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl66_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl66$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_lnkService" href="displayService.aspx?id=147727">Falconer Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_lblAddress" class="regtext">6675 Falconer Dr, Unit 3, Mississauga, ON&nbsp;&nbsp;L5N 0C3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_lblPhone" class="regtext">905-821-3637</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl67_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl67$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_lnkService" href="displayService.aspx?id=147728">First Place Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_lblAddress" class="regtext">First Medical Place, 170 Queensway W, Unit 101, Mississauga, ON&nbsp;&nbsp;L5B 3A8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_lblPhone" class="regtext">905-848-3222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl68_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl68$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_lnkService" href="displayService.aspx?id=147729">Floradale Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_lblAddress" class="regtext">2444 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5B 2V1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_lblPhone" class="regtext">905-279-1773</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl69_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl69$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_lnkService" href="displayService.aspx?id=147712">Food Basics Pharmacy - Mississauga - Hurontario St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_lblAddress" class="regtext">2550 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5B 1N5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_lblPhone" class="regtext">905-272-2828</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl70_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl70$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_lnkService" href="displayService.aspx?id=170373">Fortinos DRUGStore Pharmacy - Oakville - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_lblAddress" class="regtext">493 Dundas St W, Oakville, ON&nbsp;&nbsp;L6M 4M2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_lblPhone" class="regtext">905-257-3749</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl71_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl71$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_lnkService" href="displayService.aspx?id=154933">Fortinos DRUGStore Pharmacy - Oakville - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_lblAddress" class="regtext">173 Lakeshore Rd W, Oakville, ON&nbsp;&nbsp;L6K 1E7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_lblPhone" class="regtext">905-845-4946</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl72_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl72$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_lnkService" href="displayService.aspx?id=154817">FreshCo Pharmacy - Georgetown - Guelph St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_lblAddress" class="regtext">325 Guelph St, Georgetown, ON&nbsp;&nbsp;L7G 4B3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_lblPhone" class="regtext">905-873-1195</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl73_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl73$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_lnkService" href="displayService.aspx?id=161815">Genesis Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_lblAddress" class="regtext">221 Miller Dr, Units 8-9, Georgetown, ON&nbsp;&nbsp;L7G 6G4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_lblPhone" class="regtext">905-873-1001</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl74_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl74$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_lnkService" href="displayService.aspx?id=160714">Georgetown Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_lblAddress" class="regtext">118 Mill St, Unit 101, Georgetown, ON&nbsp;&nbsp;L7G 2C5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_lblPhone" class="regtext">905-877-8888</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl75_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl75$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_lnkService" href="displayService.aspx?id=154382">Get Well Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_lblAddress" class="regtext">1278 The Queensway, Unit 4, Toronto, ON&nbsp;&nbsp;M8Z 1S3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_lblPhone" class="regtext">416-259-4747</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl76_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl76$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_lnkService" href="displayService.aspx?id=154884">Glen Eden Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_lblAddress" class="regtext">Bronte Corporation Centre, 400 Bronte St S, Unit 102, Milton, ON&nbsp;&nbsp;L9T 0H7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_lblPhone" class="regtext">905-878-5111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl77_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl77$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_lnkService" href="displayService.aspx?id=147731">Glen Gate Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_lblAddress" class="regtext">2385 Burnhamthorpe Rd W, Unit 6, Mississauga, ON&nbsp;&nbsp;L5L 6A4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_lblPhone" class="regtext">905-820-5551</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl78_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl78$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_lnkService" href="displayService.aspx?id=154923">Glenashton Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_lblAddress" class="regtext">333 Glenashton Dr, Unit 1, Oakville, ON&nbsp;&nbsp;L6H 7P6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_lblPhone" class="regtext">905-842-2300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl79_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl79$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_lnkService" href="displayService.aspx?id=147733">Glenn Huron Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_lblAddress" class="regtext">1 Glenn Hawthorne Blvd, Unit 5, Mississauga, ON&nbsp;&nbsp;L5R 0C2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_lblPhone" class="regtext">905-890-0303</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl80_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl80$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_lnkService" href="displayService.aspx?id=147737">Greenfield Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_lblAddress" class="regtext">1053 Dundas St W, Mississauga, ON&nbsp;&nbsp;L5C 1C3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_lblPhone" class="regtext">905-306-1212</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl81_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl81$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_lnkService" href="displayService.aspx?id=153468">Guardian Pharmacy - Etobicoke - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_lblAddress" class="regtext">5468 Dundas St W, Suite 104, Toronto, ON&nbsp;&nbsp;M9B 6E3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_lblPhone" class="regtext">647-725-5143</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl82_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl82$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_lnkService" href="displayService.aspx?id=153288">Guardian Pharmacy - Etobicoke - Eringate Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_lblAddress" class="regtext">BMO Plaza, 120 Eringate Dr, Toronto, ON&nbsp;&nbsp;M9C 3Z8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_lblPhone" class="regtext">416-621-3111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl83_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl83$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_lnkService" href="displayService.aspx?id=154826">Guardian Pharmacy - Georgetown - Main St S (Young's Pharmacy and Homecare)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_lblAddress" class="regtext">47 Main St S, Georgetown, ON&nbsp;&nbsp;L7G 3G2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_lblPhone" class="regtext">905-877-2711</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl84_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl84$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_lnkService" href="displayService.aspx?id=176150">Guardian Pharmacy - Georgetown - Mountainview Rd S (Mountainview Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_lblAddress" class="regtext">378 Mountainview Rd S, Unit 11, Georgetown, ON&nbsp;&nbsp;L7G 0L5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_lblPhone" class="regtext">905-877-0700</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl85_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl85$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl86_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl86_lnkService" href="displayService.aspx?id=172443">Guardian Pharmacy - Mississauga - 1000 Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl86_lblAddress" class="regtext">1000 Burnhamthorpe Rd W, Mississauga, ON&nbsp;&nbsp;L5C 2S4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl86_lblPhone" class="regtext">905-897-8787</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl86_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl86$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_lnkService" href="displayService.aspx?id=173990">Guardian Pharmacy - Mississauga - 720 Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_lblAddress" class="regtext">720 Burnhamthorpe Rd W, Unit 4, Mississauga, ON&nbsp;&nbsp;L5C 3G1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_lblPhone" class="regtext">905-615-7777</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl87_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl87$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_lnkService" href="displayService.aspx?id=166049">Guardian Pharmacy - Mississauga - 780 Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_lblAddress" class="regtext">780 Burnhamthorpe Rd W, Unit 4, Mississauga, ON&nbsp;&nbsp;L5C 3X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_lblPhone" class="regtext">905-273-5666</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl88_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl88$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_lnkService" href="displayService.aspx?id=163145">Guardian Pharmacy - Mississauga - Britannia Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_lblAddress" class="regtext">Janpath Plaza, 812 Britannia Rd W, Unit 109, Mississauga, ON&nbsp;&nbsp;L5V 0A6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_lblPhone" class="regtext">905-812-0777</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl89_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl89$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_lnkService" href="displayService.aspx?id=147781">Guardian Pharmacy - Mississauga - Credit Valley Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_lblAddress" class="regtext">2180 Credit Valley Rd, Mississauga, ON&nbsp;&nbsp;L5M 3C9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_lblPhone" class="regtext">905-820-5434</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl90_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl90$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_lnkService" href="displayService.aspx?id=165059">Guardian Pharmacy - Mississauga - Dundas St W (Dundas Medical Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_lblAddress" class="regtext">1224 Dundas St W, Unit 107, Mississauga, ON&nbsp;&nbsp;L5C 4G7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_lblPhone" class="regtext">905-275-8500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl91_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl91$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_lnkService" href="displayService.aspx?id=166318">Guardian Pharmacy - Mississauga - Dundas St W (Medi Plus Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_lblAddress" class="regtext">777 Dundas St W, Mississauga, ON&nbsp;&nbsp;L5C 4S8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_lblPhone" class="regtext">905-279-6970</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl92_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl92$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_lnkService" href="displayService.aspx?id=147748">Guardian Pharmacy - Mississauga - Eglinton Ave E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_lblAddress" class="regtext">295 Eglinton Ave E, Unit 9, Mississauga, ON&nbsp;&nbsp;L4Z 3K6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_lblPhone" class="regtext">905-712-4231</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl93_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl93$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_lnkService" href="displayService.aspx?id=147706">Guardian Pharmacy - Mississauga - Enfield Place</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_lblAddress" class="regtext">265 Enfield Place, Unit R210, Mississauga, ON&nbsp;&nbsp;L5B 3Y6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_lblPhone" class="regtext">905-276-9488</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl94_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl94$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_lnkService" href="displayService.aspx?id=147741">Guardian Pharmacy - Mississauga - Heritage Hills Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_lblAddress" class="regtext">4646 Heritage Hills Blvd, Units 9-10, Mississauga, ON&nbsp;&nbsp;L5R 1Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_lblPhone" class="regtext">905-890-1556</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl95_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl95$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_lnkService" href="displayService.aspx?id=147754">Guardian Pharmacy - Mississauga - Kingsbridge Garden Circle</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_lblAddress" class="regtext">20 Kingsbridge Garden Circle, Unit 2, Mississauga, ON&nbsp;&nbsp;L5R 3K7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_lblPhone" class="regtext">905-568-0022</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl96_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl96$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_lnkService" href="displayService.aspx?id=147767">Guardian Pharmacy - Mississauga - Lakeshore Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_lblAddress" class="regtext">374 Lakeshore Rd E, Mississauga, ON&nbsp;&nbsp;L5G 1H5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_lblPhone" class="regtext">905-271-6699</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl97_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl97$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_lnkService" href="displayService.aspx?id=176185">Guardian Pharmacy - Mississauga - Lorne Park Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_lblAddress" class="regtext">1107 Lorne Park Rd, Unit 11, Mississauga, ON&nbsp;&nbsp;L5H 3A1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_lblPhone" class="regtext">905-891-1111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl98_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl98$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_lnkService" href="displayService.aspx?id=176197">Guardian Pharmacy - Mississauga - Montevideo Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_lblAddress" class="regtext">6700 Montevideo Rd, Unit 6, Mississauga, ON&nbsp;&nbsp;L5N 1V1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_lblPhone" class="regtext">905-814-5551</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl99_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl99$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_lnkService" href="displayService.aspx?id=154906">Guardian Pharmacy - Oakville - Cornwall Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_lblAddress" class="regtext">469 Cornwall Rd, Oakville, ON&nbsp;&nbsp;L6J 7S8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_lblPhone" class="regtext">905-845-8999</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl100_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl100$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_lnkService" href="displayService.aspx?id=154907">Guardian Pharmacy - Oakville - Dundas St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_lblAddress" class="regtext">338 Dundas St E, Oakville, ON&nbsp;&nbsp;L6H 6Z9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_lblPhone" class="regtext">905-257-1277</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl101_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl101$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_lnkService" href="displayService.aspx?id=154929">Guardian Pharmacy - Oakville - Lakeshore Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_lblAddress" class="regtext">347 Lakeshore Rd E, Oakville, ON&nbsp;&nbsp;L6J 1J5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_lblPhone" class="regtext">905-338-1919</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl102_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl102$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_lnkService" href="displayService.aspx?id=154950">Guardian Pharmacy - Oakville - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_lblAddress" class="regtext">2222 Lakeshore Rd W, Unit 2220, Oakville, ON&nbsp;&nbsp;L6L 5G5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_lblPhone" class="regtext">905-847-8200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl103_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl103$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_lnkService" href="displayService.aspx?id=154904">Guardian Pharmacy - Oakville - Trafalgar Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_lblAddress" class="regtext">Trafalgar Professional Centre, 1235 Trafalgar Rd, Oakville, ON&nbsp;&nbsp;L6H 3P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_lblPhone" class="regtext">905-845-0800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl104_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl104$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_lnkService" href="displayService.aspx?id=154905">Guardian Pharmacy - Oakville - Wyecroft Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_lblAddress" class="regtext">3455 Wyecroft Rd, Oakville, ON&nbsp;&nbsp;L6L 0B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_lblPhone" class="regtext">905-469-6523</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl105_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl105$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_lnkService" href="displayService.aspx?id=147739">Guru Nanak Dev Pharmacentre</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_lblAddress" class="regtext">Trillium Health Partners, Credit Valley Hospital, 2200 Eglinton Ave W, Mississauga, ON&nbsp;&nbsp;L5M 2N1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_lblPhone" class="regtext">905-813-3970 or 905-813-1100 ext 3970</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl106_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl106$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_lnkService" href="displayService.aspx?id=154924">Halton Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_lblAddress" class="regtext">Oakville Health Centre (The), 1060 Speers Rd, Suite 112, Oakville, ON&nbsp;&nbsp;L6L 2X4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_lblPhone" class="regtext">905-842-4266</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl107_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl107$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_lnkService" href="displayService.aspx?id=183020">Hanin Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_lblAddress" class="regtext">333 Dundas St E, Suite 103, Mississauga, ON&nbsp;&nbsp;L5A 1X1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_lblPhone" class="regtext">905-306-7878</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl108_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl108$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_lnkService" href="displayService.aspx?id=154885">Hawthorne Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_lblAddress" class="regtext">Hawthorne Village Square Plaza, 10220 Derry Rd, Unit 105A, Milton, ON&nbsp;&nbsp;L9T 7J3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_lblPhone" class="regtext">905-878-9292</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl109_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl109$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_lnkService" href="displayService.aspx?id=172768">Healing Hands Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_lblAddress" class="regtext">3105 Winston Churchill Blvd, Unit 22, Mississauga, ON&nbsp;&nbsp;L5L 5S3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_lblPhone" class="regtext">905-997-0153</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl110_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl110$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_lnkService" href="displayService.aspx?id=174719">Health Plus Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_lblAddress" class="regtext">640 Eglinton Ave W, Unit 3, Mississauga, ON&nbsp;&nbsp;L5R 3V2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_lblPhone" class="regtext">905-890-2040</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl111_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl111$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_lnkService" href="displayService.aspx?id=187144">Heartland Health Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_lblAddress" class="regtext">Heartland Town Centre, 775 Britannia Rd W, Unit 12, Mississauga, ON&nbsp;&nbsp;L5V 2Y1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_lblPhone" class="regtext">905-919-2200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl112_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl112$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_lnkService" href="displayService.aspx?id=147740">Heritage Glen Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_lblAddress" class="regtext">6515 Glen Erin Dr, Mississauga, ON&nbsp;&nbsp;L5N 8P9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_lblPhone" class="regtext">905-567-5800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl113_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl113$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_lnkService" href="displayService.aspx?id=147743">Hooper's Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_lblAddress" class="regtext">88 Lakeshore Rd E, Mississauga, ON&nbsp;&nbsp;L5G 1E1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_lblPhone" class="regtext">905-278-4242</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl114_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl114$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_lnkService" href="displayService.aspx?id=153455">IDA Pharmacy - Etobicoke - Renforth Dr (Renforth Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_lblAddress" class="regtext">Renforth Plaza, 460 Renforth Dr, Unit 10, Toronto, ON&nbsp;&nbsp;M9C 2N2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_lblPhone" class="regtext">416-622-0300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl115_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl115$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_lnkService" href="displayService.aspx?id=190718">IDA Pharmacy - Etobicoke - Sherway Dr (Queensway Health Pharmacentre)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_lblAddress" class="regtext">150 Sherway Dr, Etobicoke, ON&nbsp;&nbsp;M9C 1A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_lblPhone" class="regtext">416-521-4111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl116_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl116$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_lnkService" href="displayService.aspx?id=153289">IDA Pharmacy - Etobicoke - The West Mall (Glen Cade Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_lblAddress" class="regtext">The West Mall Shopping Centre, 290 The West Mall, Toronto, ON&nbsp;&nbsp;M9C 1C6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_lblPhone" class="regtext">416-622-2111<br>416-622-2220</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl117_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl117$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_lnkService" href="displayService.aspx?id=170676">IDA Pharmacy - Georgetown - Guelph St (King Cove Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_lblAddress" class="regtext">King's Cove Place, 156 Guelph St, Unit 4, Georgetown, ON&nbsp;&nbsp;L7G 4A6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_lblPhone" class="regtext">905-873-8880</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl118_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl118$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_lnkService" href="displayService.aspx?id=147688">IDA Pharmacy - Mississauga - 1207 Hurontario St (Carl's Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_lblAddress" class="regtext">1207 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5G 3H2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_lblPhone" class="regtext">905-278-7041</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl119_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl119$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_lnkService" href="displayService.aspx?id=147722">IDA Pharmacy - Mississauga - 2555 Erin Centre Blvd (Erin Centre Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_lblAddress" class="regtext">2555 Erin Centre Blvd, Unit 16, Mississauga, ON&nbsp;&nbsp;L5M 5H1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_lblPhone" class="regtext">905-816-9300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl120_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl120$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_lnkService" href="displayService.aspx?id=147683">IDA Pharmacy - Mississauga - Battleford Rd (Battleford Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_lblAddress" class="regtext">6405 Erin Mills Pkwy, Unit A-01, Mississauga, ON&nbsp;&nbsp;L5N 4H4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_lblPhone" class="regtext">905-858-1600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl121_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl121$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_lnkService" href="displayService.aspx?id=147859">IDA Pharmacy - Mississauga - Central Pkwy W (Unicare Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_lblAddress" class="regtext">325 Central Pkwy W, Unit 29, Mississauga, ON&nbsp;&nbsp;L5B 3X9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_lblPhone" class="regtext">905-361-1335</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl122_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl122$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_lnkService" href="displayService.aspx?id=161094">IDA Pharmacy - Mississauga - Confederation Pkwy (Parkside Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_lblAddress" class="regtext">4062 Confederation Pkwy, Mississauga, ON&nbsp;&nbsp;L5B 0G4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_lblPhone" class="regtext">289-914-0099</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl123_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl123$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_lnkService" href="displayService.aspx?id=147875">IDA Pharmacy - Mississauga - Credit Woodlands (Woodland IDA Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_lblAddress" class="regtext">3353 The Credit Woodlands, Unit 2, Mississauga, ON&nbsp;&nbsp;L5C 2K1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_lblPhone" class="regtext">905-279-5353</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl124_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl124$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_lnkService" href="displayService.aspx?id=147732">IDA Pharmacy - Mississauga - Derry Rd W (Glen Derry Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_lblAddress" class="regtext">2760 Derry Rd W, Unit 3, Mississauga, ON&nbsp;&nbsp;L5N 3N5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_lblPhone" class="regtext">289-997-3203</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl125_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl125$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_lnkService" href="displayService.aspx?id=147746">IDA Pharmacy - Mississauga - Dundas St E (Peckett's Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_lblAddress" class="regtext">60 Dundas St E, Mississauga, ON&nbsp;&nbsp;L5A 1W4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_lblPhone" class="regtext">905-270-1974</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl126_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl126$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_lnkService" href="displayService.aspx?id=147874">IDA Pharmacy - Mississauga - Dundas St W (Woodchester Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_lblAddress" class="regtext">2458 Dundas St W, Unit 13, Mississauga, ON&nbsp;&nbsp;L5K 1R8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_lblPhone" class="regtext">905-822-9500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl127_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl127$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_lnkService" href="displayService.aspx?id=166760">IDA Pharmacy - Mississauga - Eglinton Ave W (Care Plus Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_lblAddress" class="regtext">Confederation Plaza, 480 Eglinton Ave W, Unit 46, Mississauga, ON&nbsp;&nbsp;L5R 0G2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_lblPhone" class="regtext">905-502-6000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl128_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl128$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_lnkService" href="displayService.aspx?id=147723">IDA Pharmacy - Mississauga - Erin Mills Pkwy (Erin Mills Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_lblAddress" class="regtext">4099 Erin Mills Pkwy, Mississauga, ON&nbsp;&nbsp;L5L 3P9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_lblPhone" class="regtext">905-820-3761</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl129_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl129$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_lnkService" href="displayService.aspx?id=147861">IDA Pharmacy - Mississauga - Fowler Dr (Van Mills Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_lblAddress" class="regtext">1900 Fowler Dr, Unit D114, Mississauga, ON&nbsp;&nbsp;L5K 0A1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_lblPhone" class="regtext">905-403-0400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl130_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl130$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_lnkService" href="displayService.aspx?id=147850">IDA Pharmacy - Mississauga - Glen Erin Dr (Thomas Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_lblAddress" class="regtext">5636 Glen Erin Dr, Unit 2, Mississauga, ON&nbsp;&nbsp;L5M 6B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_lblPhone" class="regtext">905-819-9000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl131_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl131$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_lnkService" href="displayService.aspx?id=154394">IDA Pharmacy - Mississauga - Queen St S (Robinson Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_lblAddress" class="regtext">181 Queen St S, Mississauga, ON&nbsp;&nbsp;L5M 1L2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_lblPhone" class="regtext">905-826-1115</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl132_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl132$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_lnkService" href="displayService.aspx?id=147787">IDA Pharmacy - Mississauga - Queensway W (Mississauga Hospital Pharmacentre)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_lblAddress" class="regtext">100 Queensway W, Mississauga, ON&nbsp;&nbsp;L5B 1B8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_lblPhone" class="regtext">905-848-7599</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl133_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl133$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_lnkService" href="displayService.aspx?id=147751">IDA Pharmacy - Mississauga - Truscott Dr (Truscott Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_lblAddress" class="regtext">Park Royal Plaza, 2425 Truscott Dr, Mississauga, ON&nbsp;&nbsp;L5J 2B4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_lblPhone" class="regtext">905-822-1614</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl134_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl134$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_lnkService" href="displayService.aspx?id=154961">IDA Pharmacy - Oakville - Argus Rd (St Mark's Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_lblAddress" class="regtext">586 Argus Rd, Oakville, ON&nbsp;&nbsp;L6J 3J3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_lblPhone" class="regtext">905-845-6125</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl135_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl135$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_lnkService" href="displayService.aspx?id=196533">IDA Pharmacy - Oakville - Ford Dr (Ford Dr Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_lblAddress" class="regtext">609 Ford Dr, Unit 7, Oakville, ON&nbsp;&nbsp;L6J 7Z6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_lblPhone" class="regtext">905-845-3673</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl136_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl136$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_lnkService" href="displayService.aspx?id=162419">IDA Pharmacy - Oakville - Grosvenor St (Medicare Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_lblAddress" class="regtext">2165 Grosvenor St, Unit 3, Oakville, ON&nbsp;&nbsp;L6H 5K9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_lblPhone" class="regtext">905-338-3100</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl137_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl137$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_lnkService" href="displayService.aspx?id=154948">IDA Pharmacy - Oakville - Kerr St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_lblAddress" class="regtext">496 Kerr Street, Oakville, ON&nbsp;&nbsp;L6K 3C5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_lblPhone" class="regtext">905-844-1671</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl138_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl138$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_lnkService" href="displayService.aspx?id=192720">IDA Pharmacy - Oakville - Oak Park Blvd (Central Park Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_lblAddress" class="regtext">216 Oak Park Blvd, Unit 1, Oakville, ON&nbsp;&nbsp;L6H 7S8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_lblPhone" class="regtext">905-257-1217</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl139_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl139$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_lnkService" href="displayService.aspx?id=186211">IDA Pharmacy - Oakville - Queensbury Cres (Upper Middle Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_lblAddress" class="regtext">College Park Plaza, 1534 Queensbury Cres, Unit 2, Oakville, ON&nbsp;&nbsp;L6H 4G5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_lblPhone" class="regtext">905-815-9111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl140_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl140$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_lnkService" href="displayService.aspx?id=154958">IDA Pharmacy - Oakville - Third Line (Royal Oak Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_lblAddress" class="regtext">Sun Valley Square, 2524 Third Line, Unit 1, Oakville, ON&nbsp;&nbsp;L6M 0G8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_lblPhone" class="regtext">905-469-8830</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl141_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl141$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_lnkService" href="displayService.aspx?id=154887">James Snow Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_lblAddress" class="regtext">51 James Snow Pkwy N, Unit C3, Milton, ON&nbsp;&nbsp;L9T 0R3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_lblPhone" class="regtext">905-636-1799</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl142_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl142$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_lnkService" href="displayService.aspx?id=147785">JC Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_lblAddress" class="regtext">888 Dundas St E, Unit B4-2, Mississauga, ON&nbsp;&nbsp;L4Y 4G6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_lblPhone" class="regtext">905-897-3320</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl143_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl143$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_lnkService" href="displayService.aspx?id=147749">Jennas Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_lblAddress" class="regtext">796 Burnhamthorpe Rd W, Unit 2, Mississauga, ON&nbsp;&nbsp;L5C 2R9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_lblPhone" class="regtext">905-306-0111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl144_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl144$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_lnkService" href="displayService.aspx?id=147752">Kennedy Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_lblAddress" class="regtext">510 Driftcurrent Dr, Unit 6, Mississauga, ON&nbsp;&nbsp;L4Z 4B4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_lblPhone" class="regtext">905-568-1900</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl145_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl145$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_lnkService" href="displayService.aspx?id=147753">King Medical Arts Pharmacy and Home Healthcare</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_lblAddress" class="regtext">71 King St W, Suite 100, Mississauga, ON&nbsp;&nbsp;L5B 4A2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_lblPhone" class="regtext">905-270-2226</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl146_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl146$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_lnkService" href="displayService.aspx?id=154928">Kingsway Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_lblAddress" class="regtext">2828 Kingsway Dr, Unit 9, Oakville, ON&nbsp;&nbsp;L6J 7M2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_lblPhone" class="regtext">416-845-0374</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl147_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl147$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_lnkService" href="displayService.aspx?id=178267">KJK Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_lblAddress" class="regtext">1100 Dundas St W, Unit 6, Mississauga, ON&nbsp;&nbsp;L5C 4E7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_lblPhone" class="regtext">416-943-6284</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl148_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl148$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_lnkService" href="displayService.aspx?id=154930">Lakeshore Woods Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_lblAddress" class="regtext">3420 Rebecca St, Units 6-7, Oakville, ON&nbsp;&nbsp;L6L 6W2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_lblPhone" class="regtext">905-465-2626</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl149_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl149$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_lnkService" href="displayService.aspx?id=147755">Latino Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_lblAddress" class="regtext">79 Dundas St W, Unit 102, Mississauga, ON&nbsp;&nbsp;L5B 1H7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_lblPhone" class="regtext">905-277-9677</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl150_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl150$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_lnkService" href="displayService.aspx?id=147779">Life Watch Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_lblAddress" class="regtext">Cooksville Plaza, 40 Dundas St W, Unit 7A, Mississauga, ON&nbsp;&nbsp;L5B 1H4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_lblPhone" class="regtext">905-272-9191</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl151_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl151$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_lnkService" href="displayService.aspx?id=147756">Lighthouse Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_lblAddress" class="regtext">223 Lakeshore Rd E, Mississauga, ON&nbsp;&nbsp;L5G 1G5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_lblPhone" class="regtext">905-278-0747</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl152_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl152$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_lnkService" href="displayService.aspx?id=147758">Lisgar Woods Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_lblAddress" class="regtext">6970 Lisgar Dr, Unit B2, Mississauga, ON&nbsp;&nbsp;L5N 8C8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_lblPhone" class="regtext">905-824-5999</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl153_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl153$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_lnkService" href="displayService.aspx?id=171171">LMC Pharmacy - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_lblAddress" class="regtext">3075 Hospital Gate, Suite 301, Oakville, ON&nbsp;&nbsp;L6M 1M1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_lblPhone" class="regtext">289-856-9778</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl154_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl154$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_lnkService" href="displayService.aspx?id=153450">Loblaws DRUGStore Pharmacy - Etobicoke - The East Mall</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_lblAddress" class="regtext">380 The East Mall, Toronto, ON&nbsp;&nbsp;M9B 6L5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_lblPhone" class="regtext">416-695-0610</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl155_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl155$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_lnkService" href="displayService.aspx?id=147763">Loblaws DRUGStore Pharmacy - Mississauga - Glen Erin Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_lblAddress" class="regtext">5010 Glen Erin Dr, Mississauga, ON&nbsp;&nbsp;L5M 6J3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_lblPhone" class="regtext">905-607-1253</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl156_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl156$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_lnkService" href="displayService.aspx?id=170101">Loblaws DRUGStore Pharmacy - Mississauga - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_lblAddress" class="regtext">Loblaws Store, 250 Lakeshore Rd W, Mississauga, ON&nbsp;&nbsp;L5H 1G6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_lblPhone" class="regtext">905-271-3931</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl157_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl157$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_lnkService" href="displayService.aspx?id=147713">Loblaws DRUGStore Pharmacy - Mississauga - McLaughlin Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_lblAddress" class="regtext">5970 McLaughlin Rd, Mississauga, ON&nbsp;&nbsp;L5R 3X9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_lblPhone" class="regtext">905-568-4143</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl158_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl158$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_lnkService" href="displayService.aspx?id=151133">Loblaws Pharmacy (NoFrills) - Etobicoke - 1020 Islington Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_lblAddress" class="regtext">1020 Islington Ave, Toronto, ON&nbsp;&nbsp;M8Z 4R3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_lblPhone" class="regtext">416-234-1204</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl159_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl159$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_lnkService" href="displayService.aspx?id=147764">Main Drug Mart - Mississauga - 3415 Dixie Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_lblAddress" class="regtext">3415 Dixie Rd, Unit 5, Mississauga, ON&nbsp;&nbsp;L4Y 2B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_lblPhone" class="regtext">905-629-1114</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl160_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl160$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_lnkService" href="displayService.aspx?id=147766">Main Drug Mart - Mississauga - Duke of York Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_lblAddress" class="regtext">3885 Duke of York Blvd, Unit 104, Mississauga, ON&nbsp;&nbsp;L5B 0E4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_lblPhone" class="regtext">905-848-4844</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl161_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl161$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_lnkService" href="displayService.aspx?id=154889">Main St Centre Pharmacy - Milton - Main St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_lblAddress" class="regtext">875 Main St E, Milton, ON&nbsp;&nbsp;L9T 3Z3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_lblPhone" class="regtext">905-875-4999 or 905-875-1980</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl162_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl162$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_lnkService" href="displayService.aspx?id=154890">Maple Medical Pharmacy - Milton - Maple Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_lblAddress" class="regtext">1079 Maple Ave, Unit 2, Milton, ON&nbsp;&nbsp;L9T 0A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_lblPhone" class="regtext">905-876-5111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl163_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl163$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_lnkService" href="displayService.aspx?id=166286">Marketplace Pharmacy - Milton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_lblAddress" class="regtext">Milton Marketplace Plaza, 1015 Bronte St S, Unit 5b, Milton, ON&nbsp;&nbsp;L9T 8X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_lblPhone" class="regtext">905-864-1600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl164_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl164$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_lnkService" href="displayService.aspx?id=147768">Marketplace Pharmacy - Mississauga</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_lblAddress" class="regtext">4555 Hurontario St, Unit C7, Mississauga, ON&nbsp;&nbsp;L4Z 3M1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_lblPhone" class="regtext">905-507-4311</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl165_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl165$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_lnkService" href="displayService.aspx?id=153451">Markland Wood Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_lblAddress" class="regtext">Markland Woods Plaza, 4335 Bloor St W, Etobicoke, ON&nbsp;&nbsp;M9C 2A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_lblPhone" class="regtext">416-621-2000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl166_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl166$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_lnkService" href="displayService.aspx?id=172688">Matthews Gate Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_lblAddress" class="regtext">3662 Hurontario St, Unit 5, Mississauga, ON&nbsp;&nbsp;L5B 1P3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_lblPhone" class="regtext">905-232-4500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl167_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl167$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_lnkService" href="displayService.aspx?id=147765">MDM Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_lblAddress" class="regtext">Dixie Road Medical Associates Clinic, 2200 Dixie Rd, Mississauga, ON&nbsp;&nbsp;L4Y 1Z4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_lblPhone" class="regtext">905-896-2424</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl168_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl168$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_lnkService" href="displayService.aspx?id=147770">Meadowvale Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_lblAddress" class="regtext">6750 Winston Churchill Blvd, Unit 9A, Mississauga, ON&nbsp;&nbsp;L5N 4C4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_lblPhone" class="regtext">905-824-0701</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl169_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl169$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_lnkService" href="displayService.aspx?id=147771">Meadowvale Professional Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_lblAddress" class="regtext">6855 Meadowvale Town Centre Circle, Mississauga, ON&nbsp;&nbsp;L5N 2Y1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_lblPhone" class="regtext">905-821-9992</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl170_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl170$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_lnkService" href="displayService.aspx?id=154936">Medcare Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_lblAddress" class="regtext">Argus Medical Centre, 581 Argus Rd, Oakville, ON&nbsp;&nbsp;L6J 3J4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_lblPhone" class="regtext">905-842-7415</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl171_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl171$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_lnkService" href="displayService.aspx?id=147772">Medical Building Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_lblAddress" class="regtext">21 Queensway W, Mississauga, ON&nbsp;&nbsp;L5B 1B6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_lblPhone" class="regtext">905-279-1360</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl172_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl172$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_lnkService" href="displayService.aspx?id=154891">Medicine Shoppe (The) - Milton - 400 Main St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_lblAddress" class="regtext">400 Main St E, Unit 112, Milton, ON&nbsp;&nbsp;L9T 4X5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_lblPhone" class="regtext">905-876-4466</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl173_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl173$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_lnkService" href="displayService.aspx?id=154943">Medicine Shoppe (The) - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_lblAddress" class="regtext">267 Lakeshore Rd E, Suite 209, Oakville, ON&nbsp;&nbsp;L6J 1H9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_lblPhone" class="regtext">905-842-2770</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl174_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl174$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_lnkService" href="displayService.aspx?id=147776">Mediplus Pharmacy 002</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_lblAddress" class="regtext">619 Lakeshore Rd E, Mississauga, ON&nbsp;&nbsp;L5G 1H9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_lblPhone" class="regtext">905-990-5454</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl175_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl175$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_lnkService" href="displayService.aspx?id=154820">Metro Pharmacy - Georgetown</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_lblAddress" class="regtext">367 Mountainview Rd S, Georgetown, ON&nbsp;&nbsp;L7G 5X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_lblPhone" class="regtext">905-702-1131</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl176_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl176$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_lnkService" href="displayService.aspx?id=154892">Metro Pharmacy - Milton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_lblAddress" class="regtext">1050 Kennedy Circle, Milton, ON&nbsp;&nbsp;L9T 0J9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_lblPhone" class="regtext">905-878-3111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl177_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl177$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_lnkService" href="displayService.aspx?id=147790">Metro Pharmacy - Mississauga - Derry Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_lblAddress" class="regtext">3221 Derry Rd W, Mississauga, ON&nbsp;&nbsp;L5N 7L7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_lblPhone" class="regtext">905-785-8300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl178_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl178$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_lnkService" href="displayService.aspx?id=147789">Metro Pharmacy - Mississauga - Erin Mills Pkwy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_lblAddress" class="regtext">Metro Sheridan Mall, 2225 Erin Mills Pkwy, Mississauga, ON&nbsp;&nbsp;L5K 1T9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_lblPhone" class="regtext">905-829-8929</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl179_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl179$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_lnkService" href="displayService.aspx?id=154392">Metro Pharmacy - Mississauga - Southdown Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_lblAddress" class="regtext">910 Southdown Rd, Mississauga, ON&nbsp;&nbsp;L5G 2Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_lblPhone" class="regtext">905-823-4900</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl180_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl180$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_lnkService" href="displayService.aspx?id=154945">Metro Pharmacy - Oakville - North Service Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_lblAddress" class="regtext">280 North Service Rd W, Unit 1A, Oakville, ON&nbsp;&nbsp;L6M 2S2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_lblPhone" class="regtext">905-337-7694</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl181_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl181$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_lnkService" href="displayService.aspx?id=154946">Metro Pharmacy - Oakville - Upper Middle Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_lblAddress" class="regtext">1011 Upper Middle Rd E, Oakville, ON&nbsp;&nbsp;L6H 4L2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_lblPhone" class="regtext">905-849-4440</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl182_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl182$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_lnkService" href="displayService.aspx?id=181997">MI Clinic Pharmacy - Mississauga - Erin Centre Blvd (Erin Mills Town Plaza)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_lblAddress" class="regtext">Erin Mills Town Plaza, 2690 Erin Centre Blvd, Unit A005, Mississauga, ON&nbsp;&nbsp;L5M 5P5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_lblPhone" class="regtext">905-828-8900</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl183_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl183$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_lnkService" href="displayService.aspx?id=188758">MI Clinic Pharmacy - Mississauga - Plantation Place</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_lblAddress" class="regtext">5055 Plantation Place, Unit C2 and C3, Mississauga, ON&nbsp;&nbsp;L5M 6J3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_lblPhone" class="regtext">905-820-8600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl184_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl184$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_lnkService" href="displayService.aspx?id=147777">Midnite Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_lblAddress" class="regtext">3025 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5A 2H1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_lblPhone" class="regtext">905-270-6100 or 905-848-2376</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl185_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl185$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_lnkService" href="displayService.aspx?id=163516">Millcreek Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_lblAddress" class="regtext">6981 Millcreek Dr, Unit 2, Mississauga, ON&nbsp;&nbsp;L5N 1N3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_lblPhone" class="regtext">289-904-0099</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl186_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl186$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_lnkService" href="displayService.aspx?id=147778">Millway Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_lblAddress" class="regtext">Millway Plaza, 3200 Erin Mills Pkwy, Units 6-7, Mississauga, ON&nbsp;&nbsp;L5L 1W8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_lblPhone" class="regtext">905-607-8587</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl187_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl187$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_lnkService" href="displayService.aspx?id=191997">Milton Life Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_lblAddress" class="regtext">100 Bronte St S, Milton, ON&nbsp;&nbsp;L9T 1Y8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_lblPhone" class="regtext">905-878-5665</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl188_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl188$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_lnkService" href="displayService.aspx?id=154893">Milton Square Pharmacy - Milton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_lblAddress" class="regtext">1225 Maple Ave, Unit 200, Milton, ON&nbsp;&nbsp;L9T 0A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_lblPhone" class="regtext">905-878-8600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl189_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl189$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_lnkService" href="displayService.aspx?id=154894">Miltowne Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_lblAddress" class="regtext">311 Commercial St, Unit 210, Milton, ON&nbsp;&nbsp;L9T 3Z9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_lblPhone" class="regtext">905-693-8002</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl190_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl190$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_lnkService" href="displayService.aspx?id=190518">Mint Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_lblAddress" class="regtext">2486 Old Bronte Rd, Suite C103, Oakville, ON&nbsp;&nbsp;L6M 0Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_lblPhone" class="regtext">905-469-4000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl191_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl191$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_lnkService" href="displayService.aspx?id=154902">MMT Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_lblAddress" class="regtext">1108 Speers Rd, Oakville, ON&nbsp;&nbsp;L6L 2X4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_lblPhone" class="regtext">905-339-0200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl192_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl192$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_lnkService" href="displayService.aspx?id=147780">NKS Health</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_lblAddress" class="regtext">130 Dundas St E, Suite 500, Mississauga, ON&nbsp;&nbsp;L5A 3V8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_lblPhone" class="regtext">905-232-2322</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl193_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl193$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_lnkService" href="displayService.aspx?id=147760">Nofrills DRUGStore Pharmacy - Mississauga - Burnhamthorpe Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_lblAddress" class="regtext">2150 Burnhamthorpe Rd W, Mississauga, ON&nbsp;&nbsp;L5L 3A2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_lblPhone" class="regtext">905-820-7775</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl194_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl194$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_lnkService" href="displayService.aspx?id=147714">Nofrills DRUGStore Pharmacy - Mississauga - Creditview Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_lblAddress" class="regtext">6085 Creditview Rd, Mississauga, ON&nbsp;&nbsp;L5V 2A8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_lblPhone" class="regtext">905-858-1866</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl195_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl195$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_lnkService" href="displayService.aspx?id=147717">Nofrills DRUGStore Pharmacy - Mississauga - Eglinton Ave W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_lblAddress" class="regtext">620 Eglinton Ave W, Mississauga, ON&nbsp;&nbsp;L5R 3V2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_lblPhone" class="regtext">905-712-9626</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl196_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl196$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_lnkService" href="displayService.aspx?id=147716">Nofrills DRUGStore Pharmacy - Mississauga - South Service Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_lblAddress" class="regtext">Dixie Outlet Mall, 1250 South Service Rd, Mississauga, ON&nbsp;&nbsp;L5E 1V4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_lblPhone" class="regtext">905-891-5004</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl197_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl197$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_lnkService" href="displayService.aspx?id=160744">Noor Healthcare Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_lblAddress" class="regtext">Dundas Towers, 165 Dundas St W, Unit 105, Mississauga, ON&nbsp;&nbsp;L5B 2N6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_lblPhone" class="regtext">905-566-1777</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl198_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl198$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_lnkService" href="displayService.aspx?id=190664">North Medafix Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_lblAddress" class="regtext">6905 Millcreek Dr, Unit 3, Mississauga, ON&nbsp;&nbsp;L5N 6A3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_lblPhone" class="regtext">289-233-9883 ext 2</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl199_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl199$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_lnkService" href="displayService.aspx?id=174292">Oak City Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_lblAddress" class="regtext">180 Oak Park Blvd, Unit 107, Oakville, ON&nbsp;&nbsp;L6H 0A6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_lblPhone" class="regtext">289-725-0505</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl200_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl200$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_lnkService" href="displayService.aspx?id=154947">Oak Park Community Pharmacy - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_lblAddress" class="regtext">River Glen Mews, 2530 Sixth Line, Oakville, ON&nbsp;&nbsp;L6H 6W5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_lblPhone" class="regtext">905-257-7245</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl201_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl201$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_lnkService" href="displayService.aspx?id=170497">Oakvillage Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_lblAddress" class="regtext">261 Oak Walk Dr, Unit J6, Oakville, ON&nbsp;&nbsp;L6H 6M3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_lblPhone" class="regtext">905-257-5200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl202_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl202$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_lnkService" href="displayService.aspx?id=154949">Oakville Town Centre Pharmacy - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_lblAddress" class="regtext">300 North Service Rd W, Unit B17, Oakville, ON&nbsp;&nbsp;L6M 2S2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_lblPhone" class="regtext">905-339-0400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl203_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl203$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_lnkService" href="displayService.aspx?id=186968">Origins Pharmacy - Milton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_lblAddress" class="regtext">725 Bront St S, Units 2-3, Milton, ON&nbsp;&nbsp;L9T 9K1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_lblPhone" class="regtext">905-636-9996</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl204_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl204$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_lnkService" href="displayService.aspx?id=169255">Origins Pharmacy and Compounding Lab - Oakville - 3075 Hospital Gate</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_lblAddress" class="regtext">North Oakville Medical Building, 3075 Hospital Gate, Unit 108, Oakville, ON&nbsp;&nbsp;L6M 1M1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_lblPhone" class="regtext">905-847-9696</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl205_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl205$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_lnkService" href="displayService.aspx?id=168344">Origins Pharmacy and Home Health Care Centre - Oakville - 3001 Hospital Gate</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_lblAddress" class="regtext">Oakville Trafalgar Memorial Hospital (OTMH), 3001 Hospital Gate, Unit 7, Level 1, Centre Block, Oakville, ON&nbsp;&nbsp;L6M 0L8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_lblPhone" class="regtext">905-847-3223</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl206_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl206$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl207_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl207_lnkService" href="displayService.aspx?id=147783">Pacific Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl207_lblAddress" class="regtext">113 Dundas St W, Mississauga, ON&nbsp;&nbsp;L5B 1H8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl207_lblPhone" class="regtext">905-803-0276</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl207_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl207$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_lnkService" href="displayService.aspx?id=169499">Palermo Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_lblAddress" class="regtext">Palermo Professional Centre, 2525 Old Bronte Rd, Unit 100, Oakville, ON&nbsp;&nbsp;L6M 4J2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_lblPhone" class="regtext">905-582-5520</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl208_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl208$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_lnkService" href="displayService.aspx?id=147784">Parkerhill Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_lblAddress" class="regtext">255 Dundas St W, Unit 6A, Mississauga, ON&nbsp;&nbsp;L5B 3B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_lblPhone" class="regtext">905-306-1000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl209_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl209$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_lnkService" href="displayService.aspx?id=176178">Peace Land Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_lblAddress" class="regtext">1020 Johnson's Lane, Unit A3, Mississauga, ON&nbsp;&nbsp;L5J 2P7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_lblPhone" class="regtext">905-855-0909</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl210_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl210$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_lnkService" href="displayService.aspx?id=162175">Pharma Docs+ - Mississauga</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_lblAddress" class="regtext">348 Lakeshore Rd E, Unit 1, Mississauga, ON&nbsp;&nbsp;L5G 1H5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_lblPhone" class="regtext">905-891-2345</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl211_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl211$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_lnkService" href="displayService.aspx?id=154383">Pharma-Docs - Etobicoke</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_lblAddress" class="regtext">4972 Dundas St W, Toronto, ON&nbsp;&nbsp;M9A 1B7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_lblPhone" class="regtext">416-233-0404</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl212_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl212$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_lnkService" href="displayService.aspx?id=153448">PharmaChoice - Etobicoke - Rathburn Rd (HealthPlex)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_lblAddress" class="regtext">452 Rathburn Rd, Unit 2, Toronto, ON&nbsp;&nbsp;M9C 3S8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_lblPhone" class="regtext">416-621-6161</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl213_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl213$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_lnkService" href="displayService.aspx?id=154822">PharmaChoice - Georgetown - 99 Sinclair Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_lblAddress" class="regtext">99 Sinclair Ave, Unit 100, Georgetown, ON&nbsp;&nbsp;L7G 5G1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_lblPhone" class="regtext">905-873-4650</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl214_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl214$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_lnkService" href="displayService.aspx?id=147769">PharmaChoice - Mississauga -  Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_lblAddress" class="regtext">790 Burnhamthorpe Rd W, Unit 2, Mississauga, ON&nbsp;&nbsp;L5C 4G3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_lblPhone" class="regtext">905-803-0200</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl215_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl215$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_lnkService" href="displayService.aspx?id=147863">PharmaChoice - Mississauga - Bristol Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_lblAddress" class="regtext">Sandalwood Shopping Centre, 50 Bristol Rd E, Unit 2-3, Mississauga, ON&nbsp;&nbsp;L4Z 3K8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_lblPhone" class="regtext">905-890-2233</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl216_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl216$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_lnkService" href="displayService.aspx?id=189788">PharmaChoice - Mississauga - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_lblAddress" class="regtext">2255 Dundas St W, Unit 104, Mississauga, ON&nbsp;&nbsp;L5K 1R6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_lblPhone" class="regtext">905-569-2228</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl217_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl217$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_lnkService" href="displayService.aspx?id=147788">PharmaChoice - Mississauga - Fieldgate Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_lblAddress" class="regtext">Forest Glen Shopping Plaza, 3427 Fieldgate Dr, Mississauga, ON&nbsp;&nbsp;L4X 2J4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_lblPhone" class="regtext">905-625-0077</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl218_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl218$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_lnkService" href="displayService.aspx?id=147742">PharmaChoice - Mississauga - Hurontario St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_lblAddress" class="regtext">2100 Hurontario St, Unit 6, Mississauga, ON&nbsp;&nbsp;L5B 1M8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_lblPhone" class="regtext">905-270-4448</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl219_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl219$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_lnkService" href="displayService.aspx?id=196296">PharmaChoice - Mississauga - Lakeshore Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_lblAddress" class="regtext">515 Lakeshore Rd E, Unit 116, Mississauga, ON&nbsp;&nbsp;L5G 1H9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_lblPhone" class="regtext">905-891-1444</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl220_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl220$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_lnkService" href="displayService.aspx?id=147697">PharmaChoice - Mississauga - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_lblAddress" class="regtext">1865 Lakeshore Rd W, Unit 12, Mississauga, ON&nbsp;&nbsp;L5J 4P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_lblPhone" class="regtext">905-403-8181</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl221_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl221$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_lnkService" href="displayService.aspx?id=147738">PharmaChoice - Mississauga - Matheson Blvd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_lblAddress" class="regtext">801 Matheson Blvd W, Unit 14, Mississauga, ON&nbsp;&nbsp;L5V 2N6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_lblPhone" class="regtext">905-502-1616</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl222_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl222$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_lnkService" href="displayService.aspx?id=147707">PharmaChoice - Mississauga - Sainte Barbara Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_lblAddress" class="regtext">Derry Village Square, 7070 Sainte Barbara Blvd, Unit 2, Mississauga, ON&nbsp;&nbsp;L5W 0E6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_lblPhone" class="regtext">905-565-0800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl223_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl223$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_lnkService" href="displayService.aspx?id=172753">Pharmacy One</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_lblAddress" class="regtext">620 Bloor St, Mississauga, ON&nbsp;&nbsp;L5A 3V9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_lblPhone" class="regtext">905-232-2333</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl224_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl224$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_lnkService" href="displayService.aspx?id=195665">PharmaEssence Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_lblAddress" class="regtext">120 Guelph St, Georgetown, ON&nbsp;&nbsp;L7G 4A4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_lblPhone" class="regtext">905-873-9666</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl225_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl225$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_lnkService" href="displayService.aspx?id=163571">Pharmasave - Etobicoke - Bloor St W (Andrew's Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_lblAddress" class="regtext">3832 Bloor St W, Toronto, ON&nbsp;&nbsp;M9B 1L1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_lblPhone" class="regtext">416-231-0007</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl226_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl226$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_lnkService" href="displayService.aspx?id=153452">Pharmasave - Etobicoke - The Queensway</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_lblAddress" class="regtext">1750 The Queensway, Unit 6, Toronto, ON&nbsp;&nbsp;M9C 5H5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_lblPhone" class="regtext">416-695-4248</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl227_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl227$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_lnkService" href="displayService.aspx?id=154821">Pharmasave - Georgetown (MedTrust Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_lblAddress" class="regtext">Georgetown Market Place, 280 Guelph St, Unit 23, Georgetown, ON&nbsp;&nbsp;L7G 4B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_lblPhone" class="regtext">905-877-8763</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl228_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl228$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_lnkService" href="displayService.aspx?id=154886">Pharmasave - Milton (Holly Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_lblAddress" class="regtext">611 Holly Ave, Unit 104, Milton, ON&nbsp;&nbsp;L9T 0K4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_lblPhone" class="regtext">905-878-9001</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl229_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl229$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_lnkService" href="displayService.aspx?id=147873">Pharmasave - Mississauga - 1151 Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_lblAddress" class="regtext">Westdale Plaza, 1151 Dundas St W, Mississauga, ON&nbsp;&nbsp;L5C 1C6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_lblPhone" class="regtext">905-276-3223</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl230_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl230$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_lnkService" href="displayService.aspx?id=169569">Pharmasave - Mississauga - 2575 Dundas St W (SureCare Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_lblAddress" class="regtext">2575 Dundas St W, Unit 15, Mississauga, ON&nbsp;&nbsp;L5K 2M6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_lblPhone" class="regtext">905-607-0786</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl231_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl231$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_lnkService" href="displayService.aspx?id=147804">Pharmasave - Mississauga - Bristol Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_lblAddress" class="regtext">1525 Bristol Rd W, Unit 14-15, Mississauga, ON&nbsp;&nbsp;L5M 4Z1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_lblPhone" class="regtext">905-819-1999</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl232_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl232$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_lnkService" href="displayService.aspx?id=147736">Pharmasave - Mississauga - Central Parkway W (Grand Park Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_lblAddress" class="regtext">719 Central Pkwy W, Unit 207, Mississauga, ON&nbsp;&nbsp;L5B 4L1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_lblPhone" class="regtext">905-270-8500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl233_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl233$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_lnkService" href="displayService.aspx?id=183026">Pharmasave - Mississauga - City Centre Dr (Square One Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_lblAddress" class="regtext">33 City Centre Dr, Unit 110, Mississauga, ON&nbsp;&nbsp;L5B 2N5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_lblPhone" class="regtext">905-277-0888</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl234_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl234$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_lnkService" href="displayService.aspx?id=147757">Pharmasave - Mississauga - Doug Leavens Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_lblAddress" class="regtext">3945 Doug Leavens Blvd, Unit J, Mississauga, ON&nbsp;&nbsp;L5N 0A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_lblPhone" class="regtext">905-824-4449</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl235_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl235$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_lnkService" href="displayService.aspx?id=147792">Pharmasave - Mississauga - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_lblAddress" class="regtext">Inverhouse Plaza, 1900 Lakeshore Rd W, Unit 7, Mississauga, ON&nbsp;&nbsp;L5J 1J7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_lblPhone" class="regtext">905-823-9178</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl236_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl236$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_lnkService" href="displayService.aspx?id=147678">Pharmasave - Mississauga - Lorne Park Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_lblAddress" class="regtext">1150 Lorne Park Dr, Mississauga, ON&nbsp;&nbsp;L5H 3A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_lblPhone" class="regtext">905-274-3689</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl237_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl237$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_lnkService" href="displayService.aspx?id=192627">Pharmasave - Mississauga - Main St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_lblAddress" class="regtext">10 Main St, Mississauga, ON&nbsp;&nbsp;L5M 1X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_lblPhone" class="regtext">905-567-1500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl238_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl238$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_lnkService" href="displayService.aspx?id=169972">Pharmasave - Mississauga - Millcreek Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_lblAddress" class="regtext">6400 Millcreek Dr, Unit 10, Mississauga, ON&nbsp;&nbsp;L5N 3E7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_lblPhone" class="regtext">905-858-6844</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl239_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl239$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_lnkService" href="displayService.aspx?id=171174">Pharmasave - Oakville - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_lblAddress" class="regtext">Dundas Market Square, 479 Dundas St W, Oakville, ON&nbsp;&nbsp;L6M 1L9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_lblPhone" class="regtext">905-257-5779</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl240_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl240$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_lnkService" href="displayService.aspx?id=154952">Pharmasave - Oakville - Upper Middle Rd W (Fairways Pharmasave)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_lblAddress" class="regtext">1500 Upper Middle Rd W, Unit 16, Oakville, ON&nbsp;&nbsp;L6M 3G3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_lblPhone" class="regtext">905-847-3130</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl241_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl241$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_lnkService" href="displayService.aspx?id=154951">PharmaSense - Oakville - Westoak Trails Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_lblAddress" class="regtext">2983 Westoak Trails Blvd, Unit 8, Oakville, ON&nbsp;&nbsp;L6M 5E4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_lblPhone" class="regtext">905-901-1216</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl242_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl242$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_lnkService" href="displayService.aspx?id=154953">Pharmex Direct</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_lblAddress" class="regtext">2333 Wyecroft Rd, Unit 8, Oakville, ON&nbsp;&nbsp;L6L 6L4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_lblPhone" class="regtext">905-847-8224</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl243_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl243$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_lnkService" href="displayService.aspx?id=147842">Prince Theodore Group of Pharmacies - Mississauga - Britannia Rd W (St Mary's Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_lblAddress" class="regtext">1201 Britannia Rd W, Mississauga, ON&nbsp;&nbsp;L5V 1N2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_lblPhone" class="regtext">905-821-4550</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl244_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl244$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_lnkService" href="displayService.aspx?id=147730">Prince Theodore Group of Pharmacies - Mississauga - Dunwin Dr (Glen Erin Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_lblAddress" class="regtext">2318 Dunwin Dr, Units 1-2, Mississauga, ON&nbsp;&nbsp;L5L 1C7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_lblPhone" class="regtext">905-828-1980</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl245_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl245$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_lnkService" href="displayService.aspx?id=147720">Prince Theodore Group of Pharmacies - Mississauga - Eglinton Ave W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_lblAddress" class="regtext">2901 Eglinton Ave W, Units C3-C4, Mississauga, ON&nbsp;&nbsp;L5M 6J3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_lblPhone" class="regtext">905-608-1100</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl246_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl246$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_lnkService" href="displayService.aspx?id=147759">Prince Theodore Group of Pharmacies - Mississauga - Living Arts Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_lblAddress" class="regtext">4100 Living Arts Dr, Unit 1, Mississauga, ON&nbsp;&nbsp;L5B 0C3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_lblPhone" class="regtext">905-279-0002</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl247_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl247$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_lnkService" href="displayService.aspx?id=154931">Prince Theodore Group of Pharmacies - Oakville - Kerr St (Leon Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_lblAddress" class="regtext">340 Kerr St, Oakville, ON&nbsp;&nbsp;L6K 3B8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_lblPhone" class="regtext">905-845-2811</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl248_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl248$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_lnkService" href="displayService.aspx?id=154927">Prince Theodore Group of Pharmacies - Oakville - Kingsridge Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_lblAddress" class="regtext">2015 Kingsridge Dr, Unit 6, Oakville, ON&nbsp;&nbsp;L6M 4Y7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_lblPhone" class="regtext">905-465-3739</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl249_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl249$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_lnkService" href="displayService.aspx?id=147793">Professional Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_lblAddress" class="regtext">Burnhamthorpe Professional Centre, 1420 Burnhamthorpe Rd E, Unit 101, Mississauga, ON&nbsp;&nbsp;L4X 2Z9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_lblPhone" class="regtext">905-625-6878</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl250_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl250$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_lnkService" href="displayService.aspx?id=179270">Quality Care Pharmacy Shepard</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_lblAddress" class="regtext">Newin Centre, 2580 Shepard Ave, Unit 33, Mississauga, ON&nbsp;&nbsp;L5A 4K3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_lblPhone" class="regtext">905-566-0800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl251_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl251$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_lnkService" href="displayService.aspx?id=170734">Queen Pharmacy (The)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_lblAddress" class="regtext">5025 Creditview Rd, Mississauga, ON&nbsp;&nbsp;L5V 3E5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_lblPhone" class="regtext">905-826-5555</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl252_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl252$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_lnkService" href="displayService.aspx?id=154954">Queen's Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_lblAddress" class="regtext">1289 Marlborough Court, Unit 5A, Oakville, ON&nbsp;&nbsp;L6H 2R9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_lblPhone" class="regtext">905-844-8811</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl253_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl253$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_lnkService" href="displayService.aspx?id=153453">Queensmed Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_lblAddress" class="regtext">220 Sherway Dr, Etobicoke, ON&nbsp;&nbsp;M9C 0A7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_lblPhone" class="regtext">416-622-8482</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl254_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl254$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_lnkService" href="displayService.aspx?id=147794">Queensway Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_lblAddress" class="regtext">101 Queensway W, Suite 100 and 150, Mississauga, ON&nbsp;&nbsp;L5B 2P7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_lblPhone" class="regtext">905-281-1400</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl255_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl255$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_lnkService" href="displayService.aspx?id=147795">Queentario Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_lblAddress" class="regtext">2325 Hurontario St, Unit 4A, Mississauga, ON&nbsp;&nbsp;L5A 4C7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_lblPhone" class="regtext">905-281-1383</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl256_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl256$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_lnkService" href="displayService.aspx?id=147797">Rathburn Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_lblAddress" class="regtext">Rathburn Plaza, 592 Rathburn Rd W, Mississauga, ON&nbsp;&nbsp;L5B 3A4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_lblPhone" class="regtext">905-897-2228</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl257_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl257$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_lnkService" href="displayService.aspx?id=154955">Ray Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_lblAddress" class="regtext">635 Fourth Line, Unit 6, Oakville, ON&nbsp;&nbsp;L6L 5W4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_lblPhone" class="regtext">905-845-5595</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl258_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl258$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_lnkService" href="displayService.aspx?id=154819">Real Canadian Superstore DRUGStore Pharmacy - Georgetown</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_lblAddress" class="regtext">171 Guelph St, Georgetown, ON&nbsp;&nbsp;L7G 4A1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_lblPhone" class="regtext">905-877-7005</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl259_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl259$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_lnkService" href="displayService.aspx?id=154888">Real Canadian Superstore DRUGStore Pharmacy - Milton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_lblAddress" class="regtext">820 Main St E, Milton, ON&nbsp;&nbsp;L9T 0J4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_lblPhone" class="regtext">905-875-3600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl260_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl260$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_lnkService" href="displayService.aspx?id=147715">Real Canadian Superstore DRUGStore Pharmacy - Mississauga - Argentia Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_lblAddress" class="regtext">3050 Argentia Rd, Mississauga, ON&nbsp;&nbsp;L5N 8E1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_lblPhone" class="regtext">905-785-0955</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl261_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl261$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_lnkService" href="displayService.aspx?id=147762">Real Canadian Superstore DRUGStore Pharmacy - Mississauga - Mavis Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_lblAddress" class="regtext">3045 Mavis Rd, Mississauga, ON&nbsp;&nbsp;L5C 1T7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_lblPhone" class="regtext">905-275-1879</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl262_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl262$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_lnkService" href="displayService.aspx?id=154934">Real Canadian Superstore DRUGStore Pharmacy - Oakville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_lblAddress" class="regtext">201 Oak Park Dr, Oakville, ON&nbsp;&nbsp;L6H 6M3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_lblPhone" class="regtext">905-257-9330</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl263_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl263$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_lnkService" href="displayService.aspx?id=154387">Remedy'sRx Pharmacy - Etobicoke (Solara Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_lblAddress" class="regtext">3857 Lakeshore Blvd W, Toronto, ON&nbsp;&nbsp;M8W 0A2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_lblPhone" class="regtext">416-259-2000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl264_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl264$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_lnkService" href="displayService.aspx?id=153454">Remedy'sRx Pharmacy - Etobicoke - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_lblAddress" class="regtext">4922 Dundas St W, Toronto, ON&nbsp;&nbsp;M9A 1B7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_lblPhone" class="regtext">416-239-8127</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl265_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl265$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_lnkService" href="displayService.aspx?id=147695">Remedy'sRx Pharmacy - Mississauga - Confederation Pkwy (City Centre)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_lblAddress" class="regtext">4175 Confederation Pkwy, Unit 1-2, Mississauga, ON&nbsp;&nbsp;L5B 0H1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_lblPhone" class="regtext">905-232-3320</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl266_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl266$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_lnkService" href="displayService.aspx?id=147694">Remedy'sRx Pharmacy - Mississauga - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_lblAddress" class="regtext">134 Dundas St W, Unit 2, Mississauga, ON&nbsp;&nbsp;L5B 1H9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_lblPhone" class="regtext">905-848-8444</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl267_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl267$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_lnkService" href="displayService.aspx?id=160976">Remedy'sRx Pharmacy - Mississauga - Laird Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_lblAddress" class="regtext">3470 Laird Rd, Unit 3, Mississauga, ON&nbsp;&nbsp;L5L 5Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_lblPhone" class="regtext">905-820-7207</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl268_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl268$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_lnkService" href="displayService.aspx?id=154393">Remedy'sRx Pharmacy - Mississauga - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_lblAddress" class="regtext">150 Lakeshore Rd W, Unit 101, Mississauga, ON&nbsp;&nbsp;L5H 3R2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_lblPhone" class="regtext">905-274-5244</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl269_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl269$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_lnkService" href="displayService.aspx?id=147745">Remedy'sRx Pharmacy - Mississauga - Matheson Blvd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_lblAddress" class="regtext">550 Matheson Blvd W, Unit 106, Mississauga, ON&nbsp;&nbsp;L5R 4B8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_lblPhone" class="regtext">905-712-0003</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl270_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl270$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_lnkService" href="displayService.aspx?id=187394">Remedy'sRx Pharmacy - Mississauga - Winston Churchill Blvd (Green Bay Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_lblAddress" class="regtext">3015 Winston Churchill Blvd, Unit 101A, Mississauga, ON&nbsp;&nbsp;L5L 2V8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_lblPhone" class="regtext">905-997-8677</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl271_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl271$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_lnkService" href="displayService.aspx?id=154925">Remedy'sRx Pharmacy - Oakville - Lakeshore Rd E (Madill Health Aid Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_lblAddress" class="regtext">290 Lakeshore Rd E, Oakville, ON&nbsp;&nbsp;L6J 1J2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_lblPhone" class="regtext">905-339-1066</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl272_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl272$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_lnkService" href="displayService.aspx?id=146762">Renew Medical Pharmacy - Misssissauga (Head Office)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_lblAddress" class="regtext">1015 Cawthra Rd, Mississauga, ON&nbsp;&nbsp;L5G 4K3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_lblPhone" class="regtext">905-271-1134</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl273_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl273$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_lnkService" href="displayService.aspx?id=154199">Rexall Pharmacy - Acton - Queen St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_lblAddress" class="regtext">372 Queen St E, Acton, ON&nbsp;&nbsp;L7J 2Y5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_lblPhone" class="regtext">519-853-2220</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl274_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl274$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_lnkService" href="displayService.aspx?id=154385">Rexall Pharmacy - Etobicoke - Brown's Line</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_lblAddress" class="regtext">440 Brown's Line, Toronto, ON&nbsp;&nbsp;M8W 3T9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_lblPhone" class="regtext">416-251-2289</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl275_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl275$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_lnkService" href="displayService.aspx?id=153456">Rexall Pharmacy - Etobicoke - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_lblAddress" class="regtext">Islington Village Toronto, 4890 Dundas St W, Toronto, ON&nbsp;&nbsp;M9A 1B5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_lblPhone" class="regtext">416-239-8360</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl276_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl276$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_lnkService" href="displayService.aspx?id=154384">Rexall Pharmacy - Etobicoke - Lakeshore Blvd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_lblAddress" class="regtext">3701 Lakeshore Blvd W, Toronto, ON&nbsp;&nbsp;M8W 1P8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_lblPhone" class="regtext">416-259-3777</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl277_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl277$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_lnkService" href="displayService.aspx?id=153463">Rexall Pharmacy - Etobicoke - Sherway Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_lblAddress" class="regtext">Queensway Professional Centre, 190 Sherway Dr, Unit 107, Toronto, ON&nbsp;&nbsp;M9C 5N2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_lblPhone" class="regtext">416-620-7677</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl278_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl278$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_lnkService" href="displayService.aspx?id=153457">Rexall Pharmacy - Etobicoke - The East Mall</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_lblAddress" class="regtext">Cloverdale Mall, 250 The East Mall, Toronto, ON&nbsp;&nbsp;M9B 3Y8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_lblPhone" class="regtext">416-239-3511</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl279_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl279$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_lnkService" href="displayService.aspx?id=154895">Rexall Pharmacy - Milton - Derry Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_lblAddress" class="regtext">6541 Derry Rd W, Milton, ON&nbsp;&nbsp;L9T 7W1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_lblPhone" class="regtext">905-876-8965</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl280_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl280$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_lnkService" href="displayService.aspx?id=147803">Rexall Pharmacy - Mississauga - Burnhamthorpe Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_lblAddress" class="regtext">Central Parkway Mall, 377 Burnhamthorpe Rd E, Mississauga, ON&nbsp;&nbsp;L5A 3Y1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_lblPhone" class="regtext">905-277-0379</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl281_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl281$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_lnkService" href="displayService.aspx?id=147801">Rexall Pharmacy - Mississauga - Creditview Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_lblAddress" class="regtext">6045 Creditview Rd, Unit F001, Mississauga, ON&nbsp;&nbsp;L5V 2A8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_lblPhone" class="regtext">905-826-0583</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl282_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl282$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_lnkService" href="displayService.aspx?id=147802">Rexall Pharmacy - Mississauga - Derry Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_lblAddress" class="regtext">3221 Derry Rd W, Unit 16, Mississauga, ON&nbsp;&nbsp;L5N 7L7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_lblPhone" class="regtext">905-785-0899</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl283_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl283$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_lnkService" href="displayService.aspx?id=147798">Rexall Pharmacy - Mississauga - Dixie Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_lblAddress" class="regtext">3100 Dixie Rd, Mississauga, ON&nbsp;&nbsp;L4Y 2A6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_lblPhone" class="regtext">905-279-6690</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl284_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl284$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_lnkService" href="displayService.aspx?id=147786">Rexall Pharmacy - Mississauga - Eglinton Ave W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_lblAddress" class="regtext">1240 Eglinton Ave W, Unit B7, Mississauga, ON&nbsp;&nbsp;L5V 1N3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_lblPhone" class="regtext">905-858-7903</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl285_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl285$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_lnkService" href="displayService.aspx?id=147799">Rexall Pharmacy - Mississauga - Southdown Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_lblAddress" class="regtext">Southdown Shopping Centre, 1375 Southdown Rd, Unit 1, Mississauga, ON&nbsp;&nbsp;L5J 2Z1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_lblPhone" class="regtext">905-822-1631</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl286_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl286$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_lnkService" href="displayService.aspx?id=147800">Rexall Pharmacy - Mississauga - Thomas St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_lblAddress" class="regtext">3010 Thomas St, Mississauga, ON&nbsp;&nbsp;L5M 0R4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_lblPhone" class="regtext">905-813-9998<br>905-813-9500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl287_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl287$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_lnkService" href="displayService.aspx?id=154917">Rexall Pharmacy - Oakville - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_lblAddress" class="regtext">Bronte Village Mall, 2441 Lakeshore Rd W, Oakville, ON&nbsp;&nbsp;L6L 1H6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_lblPhone" class="regtext">905-825-0677</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl288_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl288$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_lnkService" href="displayService.aspx?id=154956">Rexall Pharmacy - Oakville - Maple Grove Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_lblAddress" class="regtext">523 Maple Grove Rd, Oakville, ON&nbsp;&nbsp;L6J 4W3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_lblPhone" class="regtext">905-849-1660</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl289_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl289$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_lnkService" href="displayService.aspx?id=176161">River Glen Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_lblAddress" class="regtext">River Glen Plaza, 575 River Glen Blvd, Unit 8, Oakville, ON&nbsp;&nbsp;L6H 6X6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_lblPhone" class="regtext">289-837-4455</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl290_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl290$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_lnkService" href="displayService.aspx?id=154957">River Oaks Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_lblAddress" class="regtext">2163 Sixth Line, Unit A3, Oakville, ON&nbsp;&nbsp;L6H 3N7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_lblPhone" class="regtext">905-842-1113</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl291_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl291$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_lnkService" href="displayService.aspx?id=197113">Rx Connect Specialty Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_lblAddress" class="regtext">6990 Creditview Rd, Unit 4, Mississauga, ON&nbsp;&nbsp;L5N 8R9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_lblPhone" class="regtext">1-855-692-2738 (1-855-MYCARE8)</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl292_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl292$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_lnkService" href="displayService.aspx?id=188997">RXI Specialty Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_lblAddress" class="regtext">5155 Spectrum Way, Unit 29, Mississauga, ON&nbsp;&nbsp;L4W 5A1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_lblPhone" class="regtext">1-844-621-2273 (1-844-621-CARE)</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl293_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl293$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_lnkService" href="displayService.aspx?id=147805">Sadia's Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_lblAddress" class="regtext">3038 Hurontario St, Unit 2, Mississauga, ON&nbsp;&nbsp;L5B 3B9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_lblPhone" class="regtext">905-896-4642</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl294_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl294$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_lnkService" href="displayService.aspx?id=147747">Sandalwood Drugs Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_lblAddress" class="regtext">Eglinton Commercial Centre, 30 Eglinton Ave W, Unit 10B, Mississauga, ON&nbsp;&nbsp;L5R 3E7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_lblPhone" class="regtext">905-568-2628</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl295_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl295$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_lnkService" href="displayService.aspx?id=188735">Santa Maria Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_lblAddress" class="regtext">C, , ON&nbsp;&nbsp;L9T 7P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_lblPhone" class="regtext">905-878-8222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl296_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl296$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_lnkService" href="displayService.aspx?id=153458">Sav-On Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_lblAddress" class="regtext">880 Brown's Line, Toronto, ON&nbsp;&nbsp;M8W 3W2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_lblPhone" class="regtext">416-259-1175</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl297_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl297$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_lnkService" href="displayService.aspx?id=147808">Shepherd Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_lblAddress" class="regtext">1474 Pickwick Dr, Unit 5A, Mississauga, ON&nbsp;&nbsp;L5V 2G2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_lblPhone" class="regtext">905-812-5111</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl298_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl298$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_lnkService" href="displayService.aspx?id=172642">Shepherd Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_lblAddress" class="regtext">579 Kerr St, Unit 7, Oakville, ON&nbsp;&nbsp;L6K 3E1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_lblPhone" class="regtext">905-845-8777</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl299_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl299$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_lnkService" href="displayService.aspx?id=147809">Sheridan Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_lblAddress" class="regtext">1960 Dundas St W, Mississauga, ON&nbsp;&nbsp;L5K 2R9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_lblPhone" class="regtext">905-822-7500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl300_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl300$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_lnkService" href="displayService.aspx?id=154200">Shoppers Drug Mart - Acton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_lblAddress" class="regtext">252 Queen St E, Acton, ON&nbsp;&nbsp;L7J 1P6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_lblPhone" class="regtext">519-853-3346</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl301_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl301$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_lnkService" href="displayService.aspx?id=154823">Shoppers Drug Mart - Georgetown - Guelph St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_lblAddress" class="regtext">Georgetown Market Place, 265 Guelph St, Unit A, Georgetown, ON&nbsp;&nbsp;L7G 4B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_lblPhone" class="regtext">905-877-2291</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl302_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl302$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_lnkService" href="displayService.aspx?id=154824">Shoppers Drug Mart - Georgetown - Mountainview Rd S</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_lblAddress" class="regtext">333 Mountainview Rd S, Unit 1, Georgetown, ON&nbsp;&nbsp;L7G 6E8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_lblPhone" class="regtext">905-877-2299</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl303_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl303$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_lnkService" href="displayService.aspx?id=154878">Shoppers Drug Mart - Milton - Derry Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_lblAddress" class="regtext">Building B, 6951 Derry Rd W, Milton, ON&nbsp;&nbsp;L9T 7H5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_lblPhone" class="regtext">905-636-9064</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl304_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl304$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_lnkService" href="displayService.aspx?id=154879">Shoppers Drug Mart - Milton - Kennedy Circle</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_lblAddress" class="regtext">Milton East Centre, 1020 Kennedy Circle, Milton, ON&nbsp;&nbsp;L9T 5S4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_lblPhone" class="regtext">905-878-6828</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl305_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl305$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_lnkService" href="displayService.aspx?id=154880">Shoppers Drug Mart - Milton - Main St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_lblAddress" class="regtext">Carriage Square, 265 Main St E, Unit 104, Milton, ON&nbsp;&nbsp;L9T 1P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_lblPhone" class="regtext">905-878-4492</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl306_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl306$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_lnkService" href="displayService.aspx?id=154881">Shoppers Drug Mart - Milton - Nipissing Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_lblAddress" class="regtext">Milton Mall, 75 Nipissing Rd, Milton, ON&nbsp;&nbsp;L9T 1R3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_lblPhone" class="regtext">905-878-4521</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl307_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl307$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_lnkService" href="displayService.aspx?id=147826">Shoppers Drug Mart - Mississauga - 2225 Erin Mills Pkwy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_lblAddress" class="regtext">Sheridan Centre, 2225 Erin Mills Pkwy, Mississauga, ON&nbsp;&nbsp;L5K 1T9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_lblPhone" class="regtext">905-822-6621</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl308_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl308$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_lnkService" href="displayService.aspx?id=147825">Shoppers Drug Mart - Mississauga - 2470 Hurontario St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_lblAddress" class="regtext">Huron Square, 2470 Hurontario St, Mississauga, ON&nbsp;&nbsp;L5B 0H2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_lblPhone" class="regtext">905-896-2500</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl309_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl309$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_lnkService" href="displayService.aspx?id=147820">Shoppers Drug Mart - Mississauga - 3476 Glen Erin Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_lblAddress" class="regtext">3476 Glen Erin Dr, Mississauga, ON&nbsp;&nbsp;L5L 3R4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_lblPhone" class="regtext">905-820-3770</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl310_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl310$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_lnkService" href="displayService.aspx?id=147829">Shoppers Drug Mart - Mississauga - 5033 Hurontario St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_lblAddress" class="regtext">5033 Hurontario St, Mississauga, ON&nbsp;&nbsp;L4Z 3X7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_lblPhone" class="regtext">905-890-1313</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl311_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl311$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_lnkService" href="displayService.aspx?id=147810">Shoppers Drug Mart - Mississauga - 5100 Erin Mills Pkwy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_lblAddress" class="regtext">Erin Mills Town Centre, 5100 Erin Mills Pkwy, Mississauga, ON&nbsp;&nbsp;L5M 4Z5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_lblPhone" class="regtext">905-569-3939</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl312_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl312$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_lnkService" href="displayService.aspx?id=147822">Shoppers Drug Mart - Mississauga - 6040 Glen Erin Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_lblAddress" class="regtext">Glen Erin Plaza, 6040 Glen Erin Dr, Mississauga, ON&nbsp;&nbsp;L5N 3M4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_lblPhone" class="regtext">905-821-8020</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl313_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl313$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_lnkService" href="displayService.aspx?id=147832">Shoppers Drug Mart - Mississauga - Bellshire Gate</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_lblAddress" class="regtext">7235 Bellshire Gate, Mississauga, ON&nbsp;&nbsp;L5N 8A2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_lblPhone" class="regtext">905-670-3327</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl314_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl314$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_lnkService" href="displayService.aspx?id=147827">Shoppers Drug Mart - Mississauga - Bloor St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_lblAddress" class="regtext">Applewood Hills Shopping Centre, 1125 Bloor St E, Mississauga, ON&nbsp;&nbsp;L4Y 2N6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_lblPhone" class="regtext">905-279-3300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl315_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl315$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_lnkService" href="displayService.aspx?id=147837">Shoppers Drug Mart - Mississauga - Bristol Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_lblAddress" class="regtext">720 Bristol Rd W, Mississauga, ON&nbsp;&nbsp;L5R 4A3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_lblPhone" class="regtext">905-755-9696</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl316_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl316$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_lnkService" href="displayService.aspx?id=147824">Shoppers Drug Mart - Mississauga - Burnhamthorpe Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_lblAddress" class="regtext">700 Burnhamthorpe Rd E, Mississauga, ON&nbsp;&nbsp;L4Y 2X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_lblPhone" class="regtext">905-279-1812</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl317_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl317$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_lnkService" href="displayService.aspx?id=147815">Shoppers Drug Mart - Mississauga - Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_lblAddress" class="regtext">South Common Mall, 2126 Burnhamthorpe Rd W, Mississauga, ON&nbsp;&nbsp;L5L 3A2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_lblPhone" class="regtext">905-820-7660</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl318_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl318$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_lnkService" href="displayService.aspx?id=147812">Shoppers Drug Mart - Mississauga - City Centre Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_lblAddress" class="regtext">Square One Shopping Centre, 100 City Centre Dr, Unit 1-745, Mississauga, ON&nbsp;&nbsp;L5B 2C9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_lblPhone" class="regtext">905-566-7003</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl319_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl319$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_lnkService" href="displayService.aspx?id=147831">Shoppers Drug Mart - Mississauga - Clayhill Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_lblAddress" class="regtext">3029 Clayhill Rd, Mississauga, ON&nbsp;&nbsp;L5B 4L2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_lblPhone" class="regtext">905-615-8887</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl320_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl320$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_lnkService" href="displayService.aspx?id=147838">Shoppers Drug Mart - Mississauga - Credit Valley Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_lblAddress" class="regtext">Credit Valley Medical Arts Building, 2000 Credit Valley Rd, Mississauga, ON&nbsp;&nbsp;L5M 4N4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_lblPhone" class="regtext">905-820-3408</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl321_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl321$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_lnkService" href="displayService.aspx?id=147833">Shoppers Drug Mart - Mississauga - Creditview Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_lblAddress" class="regtext">5425 Creditview Rd, Unit 1, Mississauga, ON&nbsp;&nbsp;L5V 2P3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_lblPhone" class="regtext">905-858-8711</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl322_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl322$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_lnkService" href="displayService.aspx?id=147819">Shoppers Drug Mart - Mississauga - Dixie Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_lblAddress" class="regtext">Rockwood Mall, 4141 Dixie Rd, Unit 22F, Mississauga, ON&nbsp;&nbsp;L4W 1V5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_lblPhone" class="regtext">905-625-4130</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl323_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl323$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_lnkService" href="displayService.aspx?id=147811">Shoppers Drug Mart - Mississauga - Grand Park Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_lblAddress" class="regtext">3980 Grand Park Dr, Mississauga, ON&nbsp;&nbsp;L5B 4M6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_lblPhone" class="regtext">905-566-9600</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl324_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl324$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_lnkService" href="displayService.aspx?id=147823">Shoppers Drug Mart - Mississauga - Lakeshore Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_lblAddress" class="regtext">579 Lakeshore Rd E, Unit A, Mississauga, ON&nbsp;&nbsp;L5G 1H9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_lblPhone" class="regtext">905-278-5506</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl325_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl325$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_lnkService" href="displayService.aspx?id=147836">Shoppers Drug Mart - Mississauga - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_lblAddress" class="regtext">321 Lakeshore Rd W, Mississauga, ON&nbsp;&nbsp;L5H 1G9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_lblPhone" class="regtext">905-271-4581</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl326_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl326$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_lnkService" href="displayService.aspx?id=147828">Shoppers Drug Mart - Mississauga - McLaughlin Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_lblAddress" class="regtext">7070 McLaughlin Rd, Mississauga, ON&nbsp;&nbsp;L5W 1W7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_lblPhone" class="regtext">905-696-9791</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl327_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl327$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_lnkService" href="displayService.aspx?id=147817">Shoppers Drug Mart - Mississauga - Meadowvale Town Centre Circle</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_lblAddress" class="regtext">Meadowvale Town Centre, 6975 Meadowvale Town Centre Circle, Mississauga, ON&nbsp;&nbsp;L5N 2W7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_lblPhone" class="regtext">905-826-7112</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl328_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl328$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_lnkService" href="displayService.aspx?id=147816">Shoppers Drug Mart - Mississauga - Mississauga Valley Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_lblAddress" class="regtext">Iona Square Shopping Centre, 1585 Mississauga Valley Blvd, Mississauga, ON&nbsp;&nbsp;L5A 3W9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_lblPhone" class="regtext">905-272-1100</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl329_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl329$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_lnkService" href="displayService.aspx?id=147813">Shoppers Drug Mart - Mississauga - North Service Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_lblAddress" class="regtext">Applewood Village Plaza, 1077 North Service Rd, Unit 21, Mississauga, ON&nbsp;&nbsp;L4Y 1A6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_lblPhone" class="regtext">905-277-3661</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl330_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl330$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_lnkService" href="displayService.aspx?id=147834">Shoppers Drug Mart - Mississauga - Queen St S</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_lblAddress" class="regtext">128 Queen St S, Mississauga, ON&nbsp;&nbsp;L5M 1K8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_lblPhone" class="regtext">905-567-0744</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl331_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl331$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_lnkService" href="displayService.aspx?id=147821">Shoppers Drug Mart - Mississauga - Rathburn Rd E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_lblAddress" class="regtext">Kingsbury Centre, 1891 Rathburn Rd E, Mississauga, ON&nbsp;&nbsp;L4W 3Z3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_lblPhone" class="regtext">905-624-1895</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl332_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl332$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_lnkService" href="displayService.aspx?id=147814">Shoppers Drug Mart - Mississauga - Southdown Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_lblAddress" class="regtext">Clarkson Crossing, 920 Southdown Rd, Unit 1, Mississauga, ON&nbsp;&nbsp;L5J 2Y4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_lblPhone" class="regtext">905-823-8260</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl333_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl333$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_lnkService" href="displayService.aspx?id=147830">Shoppers Drug Mart - Mississauga - Tenth Line W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_lblAddress" class="regtext">Brittany Glen Centre, 5602 Tenth Line W, Unit 101, Mississauga, ON&nbsp;&nbsp;L5M 5S5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_lblPhone" class="regtext">905-858-4618</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl334_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl334$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_lnkService" href="displayService.aspx?id=147835">Shoppers Drug Mart - Mississauga - Winston Churchill Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_lblAddress" class="regtext">3163 Winston Churchill Blvd, Mississauga, ON&nbsp;&nbsp;L5L 2W1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_lblPhone" class="regtext">905-607-7871</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl335_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl335$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_lnkService" href="displayService.aspx?id=154908">Shoppers Drug Mart - Oakville - Cornwall Rd (Olde Oakville Marketplace)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_lblAddress" class="regtext">Olde Oakville Marketplace, 351 Cornwall Rd, Oakville, ON&nbsp;&nbsp;L6J 7Z5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_lblPhone" class="regtext">905-842-2327</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl336_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl336$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_lnkService" href="displayService.aspx?id=154912">Shoppers Drug Mart - Oakville - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_lblAddress" class="regtext">478 Dundas St W, Oakville, ON&nbsp;&nbsp;L6H 6Y3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_lblPhone" class="regtext">905-257-9737</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl337_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl337$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_lnkService" href="displayService.aspx?id=154913">Shoppers Drug Mart - Oakville - Kerr St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_lblAddress" class="regtext">Oaktown Plaza, 550 Kerr St, Oakville, ON&nbsp;&nbsp;L6K 3C7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_lblPhone" class="regtext">905-845-6674</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl338_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl338$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_lnkService" href="displayService.aspx?id=154909">Shoppers Drug Mart - Oakville - Lakeshore Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_lblAddress" class="regtext">2297 Lakeshore Rd W, Oakville, ON&nbsp;&nbsp;L6L 1H2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_lblPhone" class="regtext">905-827-1561</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl339_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl339$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_lnkService" href="displayService.aspx?id=154910">Shoppers Drug Mart - Oakville - Leighland Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_lblAddress" class="regtext">Oakville Place, 240 Leighland Ave, Unit 109A, Oakville, ON&nbsp;&nbsp;L6H 3H6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_lblPhone" class="regtext">905-842-3730</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl340_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl340$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_lnkService" href="displayService.aspx?id=154914">Shoppers Drug Mart - Oakville - Prince Michael Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_lblAddress" class="regtext">Shoppes on Dundas Plaza, 2525 Prince Michael Dr, Oakville, ON&nbsp;&nbsp;L6H 0E9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_lblPhone" class="regtext">905-257-3938</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl341_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl341$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_lnkService" href="displayService.aspx?id=154915">Shoppers Drug Mart - Oakville - Rebecca St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_lblAddress" class="regtext">South Oakville Centre, 1515 Rebecca St, Oakville, ON&nbsp;&nbsp;L6L 5G8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_lblPhone" class="regtext">905-827-4141</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl342_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl342$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_lnkService" href="displayService.aspx?id=154911">Shoppers Drug Mart - Oakville - Third Line</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_lblAddress" class="regtext">B1, 2501 Third Line, Oakville, ON&nbsp;&nbsp;L6M 5A9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_lblPhone" class="regtext">905-465-3000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl343_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl343$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_lnkService" href="displayService.aspx?id=154916">Shoppers Drug Mart - Oakville - Upper Middle Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_lblAddress" class="regtext">Upper Oakville Shopping Centre, 1011 Upper Middle Rd E, Unit D5, Oakville, ON&nbsp;&nbsp;L6H 4L3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_lblPhone" class="regtext">905-842-3934</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl344_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl344$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_lnkService" href="displayService.aspx?id=153449">Shoppers Drug Mart - Toronto (Etobicoke) - Burnhamthorpe Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_lblAddress" class="regtext">Burnhamthorpe Mall, 666 Burnhamthorpe Rd, Toronto, ON&nbsp;&nbsp;M9C 2Z4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_lblPhone" class="regtext">416-620-4867</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl345_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl345$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_lnkService" href="displayService.aspx?id=162544">Shoppers Drug Mart - Toronto (Etobicoke) - Dundas St W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_lblAddress" class="regtext">Six Points Plaza, 5230 Dundas St W, Toronto, ON&nbsp;&nbsp;M9B 1A8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_lblPhone" class="regtext">416-233-3269</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl346_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl346$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_lnkService" href="displayService.aspx?id=176063">Shoppers Drug Mart - Toronto (Etobicoke) - Islington Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_lblAddress" class="regtext">Thorncrest Plaza, 1500 Islington Ave, Toronto, ON&nbsp;&nbsp;M9A 3L8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_lblPhone" class="regtext">416-239-2309</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl347_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl347$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_lnkService" href="displayService.aspx?id=154386">Shoppers Drug Mart - Toronto (Etobicoke) - Lakeshore Blvd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_lblAddress" class="regtext">3730 Lake Shore Blvd W, Unit 102, Toronto, ON&nbsp;&nbsp;M8W 1N6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_lblPhone" class="regtext">416-255-5243</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl348_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl348$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_lnkService" href="displayService.aspx?id=153461">Shoppers Drug Mart - Toronto (Etobicoke) - Lloyd Manor Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_lblAddress" class="regtext">Lloyd Manor Plaza, 201 Lloyd Manor Rd, Toronto, ON&nbsp;&nbsp;M9B 6H6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_lblPhone" class="regtext">416-236-1131</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl349_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl349$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_lnkService" href="displayService.aspx?id=153460">Shoppers Drug Mart - Toronto (Etobicoke) - The East Mall</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_lblAddress" class="regtext">600 The East Mall, Unit 1, Toronto, ON&nbsp;&nbsp;M9B 4S1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_lblPhone" class="regtext">416-622-3253</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl350_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl350$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_lnkService" href="displayService.aspx?id=153462">Shoppers Drug Mart - Toronto (Etobicoke) - The West Mall</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_lblAddress" class="regtext">Sherway Gardens Mall, 25 The West Mall, Unit 1267, Toronto, ON&nbsp;&nbsp;M9C 1B8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_lblPhone" class="regtext">416-621-2466</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl351_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl351$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_lnkService" href="displayService.aspx?id=61124">Shoppers Simply Pharmacy - Mississauga - Derry Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_lblAddress" class="regtext">3530 Derry Rd E, Mississauga, ON&nbsp;&nbsp;L4T 4E3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_lblPhone" class="regtext">905-673-5833</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl352_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl352$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_lnkService" href="displayService.aspx?id=154195">Sobeys Pharmacy - Acton</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_lblAddress" class="regtext">372 Queen St E, Acton, ON&nbsp;&nbsp;L7J 2N3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_lblPhone" class="regtext">519-853-5112</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl353_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl353$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_lnkService" href="displayService.aspx?id=163772">Sobeys Pharmacy - Milton - Bronte St S</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_lblAddress" class="regtext">1035 Bronte St S, Milton, ON&nbsp;&nbsp;L9T 8X3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_lblPhone" class="regtext">905-636-8421</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl354_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl354$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_lnkService" href="displayService.aspx?id=147840">Sobeys Pharmacy - Mississauga - Tenth Line W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_lblAddress" class="regtext">5602 Tenth Line W, Mississauga, ON&nbsp;&nbsp;L5M 7L9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_lblPhone" class="regtext">905-858-8212</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl355_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl355$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_lnkService" href="displayService.aspx?id=154959">Sobeys Pharmacy - Oakville - Maple Grove Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_lblAddress" class="regtext">511 Maple Grove Dr, Oakville, ON&nbsp;&nbsp;L6J 4W3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_lblPhone" class="regtext">905-849-0446</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl356_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl356$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_lnkService" href="displayService.aspx?id=154960">Sobeys Pharmacy - Oakville - Upper Middle Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_lblAddress" class="regtext">Glen Abbey Plaza, 1500 Upper Middle Rd, Oakville, ON&nbsp;&nbsp;L6M 3G3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_lblPhone" class="regtext">905-847-3460</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl357_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl357$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl358_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl358_lnkService" href="displayService.aspx?id=147773">Specialty Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl358_lblAddress" class="regtext">Credit Valley Professional Building, 2300 Eglinton Ave W, Unit 103, Mississauga, ON&nbsp;&nbsp;L5M 2V8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl358_lblPhone" class="regtext">905-820-2100</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl358_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl358$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl359_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl359_lnkService" href="displayService.aspx?id=195692">SQ1 Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl359_lblAddress" class="regtext">411 Burnhamthorpe Rd W, Mississauga, ON&nbsp;&nbsp;L5B 0J5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl359_lblPhone" class="regtext">647-370-2503</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl359_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl359$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_lnkService" href="displayService.aspx?id=154896">St George Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_lblAddress" class="regtext">585 Ontario St S, Unit 16, Milton, ON&nbsp;&nbsp;L9T 2N2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_lblPhone" class="regtext">905-693-0044</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl360_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl360$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_lnkService" href="displayService.aspx?id=147841">St Mary Dixie Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_lblAddress" class="regtext">4120 Dixie Rd, Unit 11, Mississauga, ON&nbsp;&nbsp;L4W 4V8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_lblPhone" class="regtext">905-625-8228</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl361_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl361$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl362_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl362_lnkService" href="displayService.aspx?id=147843">Star Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl362_lblAddress" class="regtext">Newin Centre, 2580 Shepard Ave, Unit 30, Mississauga, ON&nbsp;&nbsp;L5A 4K3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl362_lblPhone" class="regtext">905-270-1095</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl362_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl362$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_lnkService" href="displayService.aspx?id=147844">Swiderski Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_lblAddress" class="regtext">3015 Parkerhill Rd, Unit 1, Mississauga, ON&nbsp;&nbsp;L5B 4B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_lblPhone" class="regtext">905-896-1919</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl363_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl363$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_lnkService" href="displayService.aspx?id=147846">Tenth Eglinton Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_lblAddress" class="regtext">5030 Tenth Line W, Unit 6, Mississauga, ON&nbsp;&nbsp;L5M 7Z5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_lblPhone" class="regtext">905-369-0410</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl364_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl364$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_lnkService" href="displayService.aspx?id=147847">Terry Fox Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_lblAddress" class="regtext">5380 Terry Fox Way, Unit 9, Mississauga, ON&nbsp;&nbsp;L5V 0A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_lblPhone" class="regtext">905-858-3020</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl365_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl365$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_lnkService" href="displayService.aspx?id=147851">Tomken Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_lblAddress" class="regtext">Tomken Plaza, 925 Rathburn Rd E, Mississauga, ON&nbsp;&nbsp;L4W 4C3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_lblPhone" class="regtext">905-270-0044</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl366_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl366$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_lnkService" href="displayService.aspx?id=147852">Tomken Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_lblAddress" class="regtext">5153 Tomken Rd, Mississauga, ON&nbsp;&nbsp;L4W 1P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_lblPhone" class="regtext">905-624-8222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl367_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl367$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_lnkService" href="displayService.aspx?id=154898">Total Health Pharmacy - Milton - Bronte St S</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_lblAddress" class="regtext">Milton Professional Centre, 470 Bronte St S, Unit 123, Milton, ON&nbsp;&nbsp;L9T 2J4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_lblPhone" class="regtext">905-876-4440</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl368_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl368$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_lnkService" href="displayService.aspx?id=154899">Total Health Pharmacy - Milton - Laurier Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_lblAddress" class="regtext">497 Laurier Ave, Milton, ON&nbsp;&nbsp;L9T 3K8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_lblPhone" class="regtext">905-878-2000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl369_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl369$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_lnkService" href="displayService.aspx?id=147853">Total Health Pharmacy - Mississauga - Dundas St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_lblAddress" class="regtext">Cracovia Square, 160 Dundas St E, Unit 102, Mississauga, ON&nbsp;&nbsp;L5A 1W4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_lblPhone" class="regtext">905-279-5151</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl370_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl370$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_lnkService" href="displayService.aspx?id=147854">Total Health Pharmacy - Mississauga - Hurontario St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_lblAddress" class="regtext">Cooksville Colonnade, 3024 Hurontario St, Unit 308, Mississauga, ON&nbsp;&nbsp;L5B 4M4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_lblPhone" class="regtext">905-848-9955</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl371_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl371$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_lnkService" href="displayService.aspx?id=147855">Total Health Pharmacy - Mississauga - South Millway</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_lblAddress" class="regtext">3405 South Millway, Unit 3, Mississauga, ON&nbsp;&nbsp;L5L 3R1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_lblPhone" class="regtext">905-820-2002</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl372_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl372$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_lnkService" href="displayService.aspx?id=154941">Total Health Pharmacy - Oakville - Morden Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_lblAddress" class="regtext">465 Morden Rd, Oakville, ON&nbsp;&nbsp;L6K 3W6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_lblPhone" class="regtext">905-845-2733</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl373_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl373$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_lnkService" href="displayService.aspx?id=154940">Total Health Pharmacy - Oakville - Nottinghill Gate</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_lblAddress" class="regtext">1131 Nottinghill Gate, Oakville, ON&nbsp;&nbsp;L6M 1K5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_lblPhone" class="regtext">905-825-2560</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl374_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl374$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_lnkService" href="displayService.aspx?id=154939">Total Health Pharmacy - Oakville - Oak Park Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_lblAddress" class="regtext">231 Oak Park Blvd, Oakville, ON&nbsp;&nbsp;L6H 7S8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_lblPhone" class="regtext">905-257-0606</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl375_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl375$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_lnkService" href="displayService.aspx?id=147857">Trelawny Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_lblAddress" class="regtext">3899 Trelawny Circle, Unit 9, Mississauga, ON&nbsp;&nbsp;L5N 6S3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_lblPhone" class="regtext">905-785-8900</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl376_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl376$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_lnkService" href="displayService.aspx?id=147858">Twain Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_lblAddress" class="regtext">735 Twain Ave, Mississauga, ON&nbsp;&nbsp;L5W 1X1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_lblPhone" class="regtext">905-696-0888</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl377_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl377$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_lnkService" href="displayService.aspx?id=186258">Uptown Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_lblAddress" class="regtext">Trafalgar Ridge Shopping Centre, 2423 Trafalgar Rd, Oakville, ON&nbsp;&nbsp;L6H 6K7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_lblPhone" class="regtext">289-837-0800</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl378_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl378$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl379_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl379_lnkService" href="displayService.aspx?id=147860">Urban Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl379_lblAddress" class="regtext">Rathburn Square, 900 Rathburn Rd W, Unit B4, Mississauga, ON&nbsp;&nbsp;L5C 4L3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl379_lblPhone" class="regtext">905-897-2210</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl379_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl379$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_lnkService" href="displayService.aspx?id=154196">Urgent Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_lblAddress" class="regtext">10 Eastern Ave, Acton, ON&nbsp;&nbsp;L7J 0A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_lblPhone" class="regtext">519-853-3712</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl380_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl380$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_lnkService" href="displayService.aspx?id=147864">Village Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_lblAddress" class="regtext">225 Lakeshore Rd E, Mississauga, ON&nbsp;&nbsp;L5G 1G8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_lblPhone" class="regtext">905-278-7237</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl381_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl381$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_lnkService" href="displayService.aspx?id=192440">Vitale Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_lblAddress" class="regtext">2340 Council Ring Rd, Unit 107, Mississauga, ON&nbsp;&nbsp;L5L 1C1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_lblPhone" class="regtext">905-820-0730</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl382_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl382$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl383_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl383_lnkService" href="displayService.aspx?id=153464">Walmart Pharmacy - Etobicoke - North Queen St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl383_lblAddress" class="regtext">165 North Queen St, Toronto, ON&nbsp;&nbsp;M9C 1A7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl383_lblPhone" class="regtext">416-239-2088</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl383_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl383$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_lnkService" href="displayService.aspx?id=154825">Walmart Pharmacy - Georgetown - Guelph St</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_lblAddress" class="regtext">300 Guelph St, Georgetown, ON&nbsp;&nbsp;L7G 4B2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_lblPhone" class="regtext">905-873-3021</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl384_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl384$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_lnkService" href="displayService.aspx?id=154900">Walmart Pharmacy - Milton - Steeles Ave E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_lblAddress" class="regtext">1280 Steeles Ave E, Milton, ON&nbsp;&nbsp;L9T 6R1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_lblPhone" class="regtext">905-864-6035</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl385_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl385$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_lnkService" href="displayService.aspx?id=147867">Walmart Pharmacy - Mississauga - Argentia Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_lblAddress" class="regtext">3155 Argentia Rd, Mississauga, ON&nbsp;&nbsp;L5N 8E1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_lblPhone" class="regtext">905-821-8222</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl386_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl386$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_lnkService" href="displayService.aspx?id=147866">Walmart Pharmacy - Mississauga - Burnhamthorpe Rd W</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_lblAddress" class="regtext">2160 Burnhamthorpe Rd W, Mississauga, ON&nbsp;&nbsp;L5L 5Z5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_lblPhone" class="regtext">905-820-5172</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl387_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl387$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_lnkService" href="displayService.aspx?id=147865">Walmart Pharmacy - Mississauga - City Centre Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_lblAddress" class="regtext">Square One Shopping Centre, 100 City Centre Dr, Mississauga, ON&nbsp;&nbsp;L5B 2C9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_lblPhone" class="regtext">905-270-8331</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl388_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl388$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_lnkService" href="displayService.aspx?id=147869">Walmart Pharmacy - Mississauga - Dundas St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_lblAddress" class="regtext">1500 Dundas St E, Mississauga, ON&nbsp;&nbsp;L4X 1L4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_lblPhone" class="regtext">905-615-1290</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl389_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl389$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_lnkService" href="displayService.aspx?id=174148">Walmart Pharmacy - Mississauga - Erin Mills Town Centre</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_lblAddress" class="regtext">5100 Erin Mills Pkwy, Mississauga, ON&nbsp;&nbsp;L5M 4Z5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_lblPhone" class="regtext">905-820-3797</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl390_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl390$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_lnkService" href="displayService.aspx?id=147868">Walmart Pharmacy - Mississauga - Matheson Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_lblAddress" class="regtext">Heartland Supercentre, 800 Matheson Blvd, Mississauga, ON&nbsp;&nbsp;L5V 2N6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_lblPhone" class="regtext">905-817-9693</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl391_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl391$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_lnkService" href="displayService.aspx?id=154938">Walmart Pharmacy - Oakville - Hays Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_lblAddress" class="regtext">235 Hays Blvd, Oakville, ON&nbsp;&nbsp;L6H 6M4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_lblPhone" class="regtext">905-257-5742</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl392_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl392$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_lnkService" href="displayService.aspx?id=175013">We Care Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_lblAddress" class="regtext">169 Dundas St E, Unit 6A, Mississauga, ON&nbsp;&nbsp;L5A 1W8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_lblPhone" class="regtext">905-275-7555</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl393_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl393$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_lnkService" href="displayService.aspx?id=153465">Wellness Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_lblAddress" class="regtext">230 Brown's Line, Etobicoke, ON&nbsp;&nbsp;M8W 3T4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_lblPhone" class="regtext">416-621-2548</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl394_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl394$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_lnkService" href="displayService.aspx?id=147871">Wellness Healthcare Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_lblAddress" class="regtext">1170 Burnhamthorpe Rd W, Unit 8, Mississauga, ON&nbsp;&nbsp;L5C 4E6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_lblPhone" class="regtext">905-270-2870</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl395_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl395$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_lnkService" href="displayService.aspx?id=147872">Wellness Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_lblAddress" class="regtext">1177 Central Pkwy W, Unit 67, Mississauga, ON&nbsp;&nbsp;L5C 4P3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_lblPhone" class="regtext">905-277-5885</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl396_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl396$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_lnkService" href="displayService.aspx?id=154937">White Oaks Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_lblAddress" class="regtext">360 Dundas St E, Unit B6, Oakville, ON&nbsp;&nbsp;L6H 6Z9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_lblPhone" class="regtext">905-257-3611</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl397_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl397$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_lnkService" href="displayService.aspx?id=177788">Whole Health Pharmacy Cooksville</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_lblAddress" class="regtext">250 Dundas St W, Unit 106, Mississauga, ON&nbsp;&nbsp;L5B 1J2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_lblPhone" class="regtext">905-275-2273</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl398_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl398$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_lnkService" href="displayService.aspx?id=176182">Windwood Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_lblAddress" class="regtext">3080 Windwood Dr, Unit 6, Mississauga, ON&nbsp;&nbsp;L5N 2K5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_lblPhone" class="regtext">905-814-1300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl399_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl399$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_lnkService" href="displayService.aspx?id=189201">Winston Churchill and Dundas Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_lblAddress" class="regtext">3018 Winston Churchill Blvd, Unit 4, Mississauga, ON&nbsp;&nbsp;L5L 2V7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_lblPhone" class="regtext">905-828-4100</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl400_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl400$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_lnkService" href="displayService.aspx?id=164117">Wyecroft Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_lblAddress" class="regtext">245 Wyecroft Rd, Unit 1, Oakville, ON&nbsp;&nbsp;L6K 3Y6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_lblPhone" class="regtext">289-817-0099</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl401_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl401$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_lnkService" href="displayService.aspx?id=147876">Your Medicine Cabinet</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_lblAddress" class="regtext">77 The Queensway W, Unit 200, Mississauga, ON&nbsp;&nbsp;L5B 1B7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_lblPhone" class="regtext">905-566-4040</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl402_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl402$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_tdIn" valign="top" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_lnkService" href="displayService.aspx?id=154901">Zak's Pharmacy - Milton - Main St E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_lblOpen" style="color:#009900;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_lblAddress" class="regtext">70 Main St E, Milton, ON&nbsp;&nbsp;L9T 1N3</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_lblPhone" class="regtext">905-875-2424</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptRegionalServices_ctl403_lnkAddToList" title="Add to clipboard" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptRegionalServices$ctl403$lnkAddToList','')">
                                        <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                        <tr>
                            <td colspan="3">
                                <br>
                            </td>
                        </tr>
                    

                    <tr>
                            <td colspan="3" bgcolor="#fff2b9">
                                <div style="float: left;">
                                    <span id="ctl00_ContentPlaceHolder1_lblServicesOutside">These services are located outside of Mississauga Halton, but provide service to Mississauga Halton.</span>
                                </div>
                            </td>
                        </tr>
                        
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_lnkService" href="displayService.aspx?id=130152">Bayshore Home Health - York Region - Specialty Pharmacy Services</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_lblAddress" class="regtext">70 Esna Park Drive, Unit 11, Markham, ON&nbsp;&nbsp;L3R 6E7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_lblPhone" class="regtext">905-474-0822</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl00_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl00$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_lnkService" href="displayService.aspx?id=150721">Blair Court Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_lblAddress" class="regtext">266 Donlands Ave, Toronto, ON&nbsp;&nbsp;M4J 5B1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_lblPhone" class="regtext">416-423-9113</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl01_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl01$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_lnkService" href="displayService.aspx?id=150819">Dawes Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_lblAddress" class="regtext">424 Dawes Rd, Toronto, ON&nbsp;&nbsp;M4B 2E9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_lblPhone" class="regtext">416-757-2242</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl02_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl02$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_lnkService" href="displayService.aspx?id=120381">Don Russell Drug Mart</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_lblAddress" class="regtext">2891 Lake Shore Blvd W, Toronto, ON&nbsp;&nbsp;M8V 1J1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_lblPhone" class="regtext">416-251-2201</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl03_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl03$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_lnkService" href="displayService.aspx?id=61138">Etobicoke Centre Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_lblAddress" class="regtext">Etobicoke Professional Centre, 40 Westmore Dr, Etobicoke, ON&nbsp;&nbsp;M9V 4C2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_lblPhone" class="regtext">416-745-3030</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl04_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl04$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_lnkService" href="displayService.aspx?id=60973">Fortinos DRUGStore Pharmacy - Etobicoke - Queens Plate Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_lblAddress" class="regtext">330 Queens Plate Dr, Etobicoke, ON&nbsp;&nbsp;M9W 7J7</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_lblPhone" class="regtext">416-745-2825</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl05_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl05$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_lnkService" href="displayService.aspx?id=61139">Grace Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_lblAddress" class="regtext">2630 Kipling Ave, Unit 7A, Etobicoke, ON&nbsp;&nbsp;M9V 4B9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_lblPhone" class="regtext">416-741-5055</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl06_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl06$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_lnkService" href="displayService.aspx?id=61140">Humber Green Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_lblAddress" class="regtext">100 Humber College Blvd, Unit 102, Toronto, ON&nbsp;&nbsp;M9V 5G4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_lblPhone" class="regtext">416-744-3434</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl07_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl07$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_lnkService" href="displayService.aspx?id=61141">John Garland Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_lblAddress" class="regtext">1701 Martin Grove Rd, Toronto, ON&nbsp;&nbsp;M9V 4N4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_lblPhone" class="regtext">416-743-3535</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl08_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl08$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_lnkService" href="displayService.aspx?id=61119">Kipling Medical Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_lblAddress" class="regtext">2687 Kipling Ave, Unit 9, Etobicoke, ON&nbsp;&nbsp;M9V 5G6</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_lblPhone" class="regtext">416-744-8825</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl09_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl09$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_lnkService" href="displayService.aspx?id=61116">Kipling Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_lblAddress" class="regtext">2141 Kipling Ave, Unit 5, Etobicoke, ON&nbsp;&nbsp;M9W 4K8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_lblPhone" class="regtext">416-743-8333</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl10_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl10$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_lnkService" href="displayService.aspx?id=151524">LMC Pharmacy - Diabetes Source</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_lblAddress" class="regtext">CNIB, 1929 Bayview Ave, Unit 107, Toronto, ON&nbsp;&nbsp;M4G 3E8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_lblPhone" class="regtext">416-640-1863</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl11_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl11$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_lnkService" href="displayService.aspx?id=61117">Mediplus Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_lblAddress" class="regtext">1111 Albion Rd, Etobicoke, ON&nbsp;&nbsp;M9V 1A9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_lblPhone" class="regtext">416-744-8264</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl12_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl12$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_lnkService" href="displayService.aspx?id=60972">Nofrills DRUGStore Pharmacy - Etobicoke - Albion Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_lblAddress" class="regtext">1530 Albion Rd, Toronto, ON&nbsp;&nbsp;M9V 1B4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_lblPhone" class="regtext">416-744-7389</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl13_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl13$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_lnkService" href="displayService.aspx?id=61122">PharmaChoice - Etobicoke - Rexdale Blvd (Woodbine Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_lblAddress" class="regtext">500 Rexdale Blvd, Unit A2, Etobicoke, ON&nbsp;&nbsp;M9W 6K5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_lblPhone" class="regtext">416-679-8711</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl14_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl14$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_lnkService" href="displayService.aspx?id=150276">Pharmasave - Scarborough - 4218 Lawrence Ave E</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_lblAddress" class="regtext">4218 Lawrence Ave E, Unit 4, Toronto, ON&nbsp;&nbsp;M1E 4X9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_lblPhone" class="regtext">416-284-4741</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl15_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl15$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_lnkService" href="displayService.aspx?id=151366">Pharmasave - York - Weston Rd (Eagle Manor Pharmacy)</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_lblAddress" class="regtext">1901 Weston Rd, Unit 19, Toronto, ON&nbsp;&nbsp;M9N 3P5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_lblPhone" class="regtext">416-241-1115</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl16_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl16$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_lnkService" href="displayService.aspx?id=61011">Rexall - Etobicoke - Wincott Dr</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_lblAddress" class="regtext">250 Wincott Dr, Etobicoke, ON&nbsp;&nbsp;M9R 2R5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_lblPhone" class="regtext">416-248-1872</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl17_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl17$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_lnkService" href="displayService.aspx?id=151671">River Hill Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_lblAddress" class="regtext">2086 Lawrence Ave W, Unit 1-2, Toronto, ON&nbsp;&nbsp;M9N 3Z9</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_lblPhone" class="regtext">416-614-6623</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl18_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl18$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_lnkService" href="displayService.aspx?id=61120">Shih Pharmacy</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_lblAddress" class="regtext">2700 Kipling Ave, Etobicoke, ON&nbsp;&nbsp;M9V 4P2</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_lblPhone" class="regtext">416-740-1623</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl19_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl19$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_lnkService" href="displayService.aspx?id=61026">Shoppers Drug Mart - Etobicoke - 1530 Albion Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_lblAddress" class="regtext">Albion Mall, 1530 Albion Rd, Etobicoke, ON&nbsp;&nbsp;M9V 1B4</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_lblPhone" class="regtext">416-741-7711</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl20_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl20$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_lnkService" href="displayService.aspx?id=61040">Shoppers Drug Mart - Etobicoke - 900 Albion Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_lblAddress" class="regtext">Bostock Plaza, 900 Albion Rd, Bldg A, Unit 1, Etobicoke, ON&nbsp;&nbsp;M9V 1A5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_lblPhone" class="regtext">416-741-2430</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl21_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl21$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_lnkService" href="displayService.aspx?id=61038">Shoppers Drug Mart - Etobicoke - Kipling Ave</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_lblAddress" class="regtext">Westway Plaza, 1735 Kipling Ave, Etobicoke, ON&nbsp;&nbsp;M9R 2Y8</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_lblPhone" class="regtext">416-247-8757</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl22_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl22$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_lnkService" href="displayService.aspx?id=61036">Shoppers Drug Mart - Etobicoke - Rexdale Blvd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_lblAddress" class="regtext">Rexdale Plaza, 123 Rexdale Blvd, Etobicoke, ON&nbsp;&nbsp;M9W 1P1</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_lblPhone" class="regtext">416-743-1645</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl23_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl23$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_lnkService" href="displayService.aspx?id=61033">Shoppers Drug Mart - Etobicoke - The Westway</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_lblAddress" class="regtext">Martinway Plaza, 415 The Westway, Block A, Unit 1, Etobicoke, ON&nbsp;&nbsp;M9R 1H5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_lblPhone" class="regtext">416-249-8344</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl24_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl24$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_lnkService" href="displayService.aspx?id=61136">Shoppers Simply Pharmacy - Etobicoke - Albion Rd</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_lblAddress" class="regtext">1525 Albion Rd, Unit 104, Etobicoke, ON&nbsp;&nbsp;M9V 5G5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_lblPhone" class="regtext">416-746-2000</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl25_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl25$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                                <tr>
                                    <td id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_tdOut" valign="middle" class="serviceListing" style="padding-right: 5px; padding-bottom: 5px;" bgcolor="#FFFFFF">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_lnkService" href="displayService.aspx?id=61121">Total Health Pharmacy - Etobicoke - Woodbine Downs</a>
                                        &nbsp;
                                        <a href="/servicesProvidedInFrench.aspx" class="noborder" style="display: none;">
                                            </a>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_lblOpen" style="color:#69BE28;">Open</span>
                                        <br>
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_lblAddress" class="regtext">25 Woodbine Downs, Etobicoke, ON&nbsp;&nbsp;M9W 6N5</span>
                                    </td>
	
                                    <td valign="top" class="serviceListingCity" width="20%">
                                        <span id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_lblPhone" class="regtext">416-674-0300</span>
                                    </td>
                                    <td valign="top" width="18%">
                                        <a id="ctl00_ContentPlaceHolder1_rptOtherServices_ctl26_lnkAddToList" title="<%= labelAddToList %>" class="utility-btns" href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$rptOtherServices$ctl26$lnkAddToList','')">
                                             <span class="icon-add-to-clipboard"></span> Add to Clipboard </a>
                                        
                                    </td>
                                </tr>
                            
                    

                
            <tr>
                <td style="padding-right: 15px">
                    <span id="ctl00_ContentPlaceHolder1_lblDisclaimer"></span>
                </td>
            </tr>
        </tbody></table>
"""

def processString(obj):
	if not obj:
		return ""
	else:
		return obj.text.strip();

def randomDelay():
	delay = random.random()*6
	print(delay)
	time.sleep(delay)

def processAddressString(address):
	return address.replace(",", " ")


filePath = 'mississauga-pharmacy.csv'
wfile = open(filePath, "w")
wfile.write('Store,phone,email,address,website\n')

# ================ First Part Get Pharmacies List ================
pharmaciesUri = []

# Parser start here
html = BeautifulSoup(response, "html.parser")

#Use find to get CSS Attribute (Single)
table = html.find("table", style="width: 100%")

tbody = table.select_one("tbody")
trs = tbody.find_all('tr')

for tr in trs[1:]:
	anchor = tr.find('td').find('a')
	if not anchor or not anchor['href']:
		continue;
	# print(anchor['href'])
	pharmaciesUri.append(anchor['href'])

# print(pharmacies)

# ================ Second Part Get Each Pharmacy Information ================
healthLineUrl = "https://www.mississaugahaltonhealthline.ca/"
for uri in pharmaciesUri:
	response = requests.get(healthLineUrl+uri)
	html = BeautifulSoup(response.text, "html.parser")

	name = processString(html.select_one('#ctl00_ContentPlaceHolder1_tdProgram'))
	phone = processString(html.select_one('#ctl00_ContentPlaceHolder1_lblOfficePhone'))
	email = processString(html.select_one('#ctl00_ContentPlaceHolder1_lnkEmail'))
	website = processString(html.select_one('#ctl00_ContentPlaceHolder1_lnkUrl'))
	address = processString(html.select_one('#ctl00_ContentPlaceHolder1_lblAddress'))

	line = name + "," + phone + "," + email + "," + processAddressString(address) + "," + website + "\n"
	wfile.write(line)
	randomDelay()

wfile.close()