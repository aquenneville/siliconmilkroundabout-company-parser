package github.aq.siliconmilkroundabout.download;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.KeyManagementException;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;

import javax.net.ssl.SSLContext;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.conn.ssl.NoopHostnameVerifier;
import org.apache.http.conn.ssl.SSLContextBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

public class HttpClient {

	private static final String USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36";
	private static ByteArrayOutputStream baos;
	private static byte[] byteArray;
	private static int statusCode;
	private static String contentType;
	private static long contentLength;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public static void executeRequest(String url) throws KeyManagementException, NoSuchAlgorithmException, KeyStoreException, ClientProtocolException, IOException {
		System.setProperty("https.protocols","TLSv1,TLSv1.1,TLSv1.2");
		SSLContext sslContext = new SSLContextBuilder()
				.loadTrustMaterial(null, (certificate, authType) -> true).build();
		
		CloseableHttpClient client = HttpClients.custom()
				.setSSLContext(sslContext)
				.setSSLHostnameVerifier(new NoopHostnameVerifier())
				.build();
		HttpGet httpGet = new HttpGet(url);
		//httpGet.setHeader("User-Agent", USER_AGENT);
		httpGet.setHeader("Accept", "text/html");
		
		HttpResponse response = client.execute(httpGet);
		
		baos = new ByteArrayOutputStream();
		response.getEntity().writeTo(baos);
		statusCode = response.getStatusLine().getStatusCode();
		contentType = response.getEntity().getContentType().getName();
		contentLength = response.getEntity().getContentLength();
		byteArray = baos.toByteArray();
	}
	
	public static byte[] getByteArray() {
		return byteArray;
	}
	
	public static int getStatusCode() {
		return statusCode;
	}
	
	public static long getContentLength() {
		return contentLength;
	}
	
	public static String getContentType() {
		return contentType;
	}
}
