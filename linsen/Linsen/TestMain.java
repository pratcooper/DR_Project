import indexing.index.IndexFactory;
import indexing.index.IndexLucene;
import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.LinkedList;
import java.util.List;
import java.util.ResourceBundle;
import java.util.Set;
import java.util.TreeSet;
import splitting.CompositeSplit;
import splitting.SplitTokenModuleFactory;

import indexing.index.analyzer.AllAnalyzer;
import indexing.index.analyzer.AllAnalyzerNormalizer;
import indexing.index.analyzer.DictionaryAnalyzer;
import indexing.index.analyzer.IdentifierAnalyzer;
import indexing.index.analyzer.IdentifierAnalyzerNormalizer;
import indexing.index.analyzer.WordAnalyzer;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.WhitespaceAnalyzer;
import java.util.HashSet;
import java.util.HashMap;

public class TestMain
{  
  public static void main(String[] args) throws IOException, RuntimeException
  {
	// String root_project = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/media/coffeemaker/1.0/coffeemaker_webzip/extracted/target_sourcefiles/";
	// String output_test_set = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/TestLinsen/TestSetDictionary/";
	// String path_token_file_test_set = "";
	// String path_stopwords_test_set= null;
	// String acronyms_file = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Acronyms.txt";
	// String abbreviations_file ="/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Abbreviations.txt";
	// String root_report = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/media/coffeemaker/1.0/coffeemaker_webzip/extracted/LINSEN_report_files/";
	// String oracle_path = "";
	// String extension_indexing_file = "java";
	// String target_file_path = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/media/coffeemaker/1.0/coffeemaker_webzip/extracted/target_sourcefiles/makecoffee.java";
	// String target_identifiers_list = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/media/coffeemaker/1.0/coffeemaker_webzip/extracted/target_identifiers.txt";
	
    String outputTestSet = ResourceBundle.getBundle("ConfigurationTestSet").getString("output_test_set");
    String pathAcronymsFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("acronyms_file");
    String rootProject = ResourceBundle.getBundle("ConfigurationTestSet").getString("root_project");
    String pathStopWordsTestSet = ResourceBundle.getBundle("ConfigurationTestSet").getString("path_stopwords_test_set");
    String pathAbbreviationsFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("abbreviations_file");
    String rootReportFolderPath = ResourceBundle.getBundle("ConfigurationTestSet").getString("root_report");
    String extensionIndexingFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("extension_indexing_file");
    String targetFilePathToAnalyse = ResourceBundle.getBundle("ConfigurationTestSet").getString("target_file_path");
    String targetIdentifersFilePath = ResourceBundle.getBundle("ConfigurationTestSet").getString("target_identifiers_list");

	LinkedList<String> externalDictionaries = new LinkedList<String>();
    
    IndexLucene targetSystemData = (IndexLucene)IndexFactory.createIndex(outputTestSet, externalDictionaries, rootProject, pathStopWordsTestSet, pathAcronymsFile, pathAbbreviationsFile, extensionIndexingFile, IndexFactory.ALL);
    System.out.println("-------------------------try to clear indexing for targetCode and Comment--------------------------------");
  	targetSystemData.deleteIndex();
    System.out.println("-------------------------Add as a new index--------------------------------");
  	targetSystemData = (IndexLucene)IndexFactory.createIndex(outputTestSet, externalDictionaries, rootProject, pathStopWordsTestSet, pathAcronymsFile, pathAbbreviationsFile, extensionIndexingFile, IndexFactory.ALL);

	//System.out.println("All words: "+targetSystemData.getAllWord());
	// CompositeSplit splitter = SplitTokenModuleFactory.createPatternMatchingSplittingModule();
   
    List<String> allFile = targetSystemData.getAllIndexedFiles();
    System.out.println("DEBUG --> Index exists: "+allFile.toString());
    
    if (!allFile.contains(targetFilePathToAnalyse)) {
    // System.out.println(target_file_path);
      System.exit(-1);
    }

    System.out.println("-------------------------try to clear indexing for splitter--------------------------------");
 //    String pathStopWords = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/StopWord.txt";
	// String outputIndex = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Structure/COFFEEMAKER/Dictionary/";
	// String dictionaries = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Informatics.txt;/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/English.txt";
	// String rootProject = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/media/coffeemaker/1.0/coffeemaker_webzip/extracted/";
	// String acronymsFilePath = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Acronyms.txt";
	// String abbreviationsFilePath = "/Users/Kamonphop/Desktop/Research_Phd/DR/code-coherence-analysis/linsen/ConfigurationFiles/Abbreviations.txt";
	// String targetFileExtensions = "java";

    String outputDictionary = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("output_dictionary");
    String[] pathDictionary = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("path_token_file_dictionary").split(";");
      

    List<String> externalDictionariesPaths = new LinkedList<String>();
    for (String p : pathDictionary) {
        if (!p.equals("")) {
            externalDictionariesPaths.add(p);
        }
    }
    String rootProjectDictionary = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("root_project_dictionary");
    String pathStopWordsDictionary = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("path_stopwords_dictionary");
    String extensionIndexing = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("extension_indexing_file");
    String pathAcronyms = ResourceBundle.getBundle("ConfigurationDictionaryforSimilarSplit").getString("acronyms_file");
    String pathAbbreviations = ResourceBundle.getBundle("ConfigurationTestSet").getString("abbreviations_file");


	// String[] pathDictionary = dictionaries.split(";");
	// List<String> externalDictionariesPaths = new LinkedList<String>();
	// 	for (String p : pathDictionary) {
	// 		if (!p.equals("")) {
	//   			externalDictionariesPaths.add(p);
	// 	}
	// }
	HashSet<String> stopWords = new HashSet<String>();
	HashSet<String> potentialAbbreviations = new HashSet<String>();

	Analyzer identifierAnalyzerNormalizer = new IdentifierAnalyzerNormalizer(pathStopWordsDictionary);
	Analyzer whiteSpaceAnalyzer = new WhitespaceAnalyzer();


	IndexLucene tempIndex = new IndexLucene(identifierAnalyzerNormalizer, whiteSpaceAnalyzer, outputDictionary, externalDictionariesPaths, rootProjectDictionary, pathAcronyms, pathAbbreviations, extensionIndexing, potentialAbbreviations, new HashMap(), new HashMap(), false, false);
    System.out.println("DEBUG --> Index exists: "+tempIndex.getAllIndexedFiles().toString());
    tempIndex.deleteIndex();
	// List<String> allFile2 = tempIndex.getAllIndexedFiles();
 //    System.out.println("Index exists: "+allFile2.toString());

	// TreeSet<String> dictionaryWords = new TreeSet();
	// for (int dIndex = 0; dIndex < externalDictionariesPaths.size(); dIndex++) {
	// 	for (String word : tempIndex.getExternalDictionary(dIndex)) {
	// 	 	dictionaryWords.add(word.toLowerCase());
	// 	}
	// }

    // String targetFilePathToAnalyse = target_file_path;
    // String targetIdentifersFilePath= target_identifiers_list;
    // String rootReportFolderPath = root_report;

    System.out.println("-------------------------Now creating the splitter object--------------------------------");

    CompositeSplit splitter = SplitTokenModuleFactory.createPatternMatchingSplittingModule();

	String targetFileName = targetFilePathToAnalyse.substring(targetFilePathToAnalyse.lastIndexOf('/') + 1, targetFilePathToAnalyse.lastIndexOf('.'));
    

    FileOutputStream reportFile = new FileOutputStream(rootReportFolderPath + targetFileName + ".txt");
    PrintStream outputReportFile = new PrintStream(reportFile);
    
    Set<String> allIdentifiers = targetSystemData.getTokenDocument(targetFilePathToAnalyse);
    //System.out.println("All Identifiers: "+allIdentifiers.toString());
    Set<String> targetIdentifiers = loadTargetIdentifiersList(targetIdentifersFilePath);
    //System.out.println("Target Identifiers: "+targetIdentifiers);

    for (String identifier : allIdentifiers) {
      if (targetIdentifiers.contains(identifier.toLowerCase())) {
        splitter.split(identifier, Integer.valueOf(1), targetFilePathToAnalyse);
        List<String> transformationMap = splitter.getTrasformationMap(identifier);
        outputReportFile.print(identifier + ":=");
        for (String token : transformationMap)
          outputReportFile.print(token + ",");
        outputReportFile.println();
      }
    }
    outputReportFile.close();


	System.out.println("-------- Done --------");
	}

    private static Set<String> loadTargetIdentifiersList(final String targetIdentifiersListFilePath) {
        final Set<String> targetIdentifiersList = new TreeSet<String>();
        try {
            final BufferedReader bufferReader = new BufferedReader(new FileReader(targetIdentifiersListFilePath));
            String line = "";
            do {
                try {
                    line = bufferReader.readLine();
                    if (line != null) {
                        targetIdentifiersList.add(line.trim().toLowerCase());
                    }
                }
                catch (IOException ioExceptionBufferedReader) {
                    break;
                }
            } while (line != null && line.length() >= 0);
        }
        catch (IOException ex) {}
        return targetIdentifiersList;
    }

}