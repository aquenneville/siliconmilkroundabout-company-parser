package github.aq.siliconmilkroundabout;

import github.aq.siliconmilkroundabout.download.CompanyPageDownloader;
import github.aq.siliconmilkroundabout.parse.CompanyParser;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

public class SiliconMilkRoundAboutCompanyParserApp {

    public static void main(String[] args) {

        String url = "";
        String timeWait = "";
        Options options = new Options();

        options.addOption(Option.builder("url")
                .required(true)
                .hasArg(true).argName("url")
                .desc("the url to get the files").build());

        options.addOption(Option.builder("time_wait")
                .required(false)
                .hasArg(true).argName("time_wait")
                .desc("the time to wait between requests in seconds").build());

        try {
            CommandLine commandLine = new DefaultParser().parse(options, args);
            url = commandLine.getOptionValue("url");
            timeWait = commandLine.getOptionValue("time_wait");

            try {				
                if (timeWait != null) {
                    CompanyPageDownloader.requestTimeWait = Integer.parseInt(timeWait);
                } 
            } catch (NumberFormatException exc) {
                exc.printStackTrace();
            }

            processDownload(url, "");
            System.out.println(CompanyPageDownloader.DownloadSummary.report());

        } catch (ParseException e) {
            HelpFormatter formatter = new HelpFormatter();
            formatter.setOptionComparator(null); // Keep insertion order of options
            formatter.printHelp(SiliconMilkRoundAboutCompanyParserApp.class.getName(), " download company files from url.", options, null);
            System.exit(1);
            return;
        }
    }

    public static void processDownload(String url, String parentPath) {
        try {
            if (CompanyPageDownloader.downloadFile(url, parentPath)) {
                if (!CompanyPageDownloader.getDownloadPath().toString().matches(CompanyParser.ALLOWED_EXTENSIONS)) {
                    List<String> listResources = CompanyParser.parseLinks(CompanyPageDownloader.getDownloadPath());
                    if (listResources.size() > 0) {
                        System.out.println("Download 1 of " + listResources.size());
                        for(String resource: listResources) {
                            if (resource.matches(CompanyParser.ALLOWED_EXTENSIONS)) {
                                if (CompanyPageDownloader.downloadFile(new URL(url).getHost() + resource, CompanyPageDownloader.getDownloadPath().toString())) {
                                    continue;
                                } else {
                                    processDownload(resource, CompanyPageDownloader.getDownloadPath().toString());
                                }
                            }
                        }
                    }
                }
            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
    }

}
